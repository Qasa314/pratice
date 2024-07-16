import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


stock_id='2330.TW'  #股票代號:2330台積電
ohlcv=yf.Ticker(stock_id).history(period='max')  #抓全部歷史資料

print(ohlcv)

x=ohlcv.tail(120).index.astype(str)
y=ohlcv.tail(120)

fig,ax=plt.subplots(figsize=(23,8),facecolor="#434343")

#變色
color1=[]
for i in y.Close-y.Open:
    if i>0:
        color1.append("#FF0000")
    else:
        color1.append("000000")
        
#印出圖片

ax.bar(x,y.Close-y.Open,0.6,y.Open,color=color1)

ax.vlines(x,y.Low,y.High,color=color1)

#移動平均線
def ma(n):
    return ohlcv.Close.rolling(n).mean(n).tail(120)

#周5/月20/季60/半年120線輸出+變色
for n,color2 in zip([5,20,60,120],['#6b90e4','#fae239','#93d557','#aa57d5']):
    ax.plot(x,ma(n),color=color2,label=f"ma{n}")
#共用X軸製圖
ax2=ax.twinx() 
#成交量直線圖
ax2.bar(x,y.Volume,color="#cccccc",alpha=0.2)


# 使用中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
#標示圖例說明
ax.set_title(f"{stock_id} 個股K線圖",fontsize=25,color='w',loc='left',y=1.1)
ax.set_xlabel('日期',fontsize=13,color='w')
ax.set_ylabel('價格',fontsize=13,color='w')
ax.tick_params('x',labelcolor='w')
ax.tick_params('y',labelcolor='w')
ax2.set_ylabel('成交量',fontsize=13,color='w')
ax2.tick_params('y',labelcolor='w')



#美化圖片+敘述
ax.text(x[1],y.Close.mean(),
        f"{y.index[-1].strftime('%Y-%m-%d')}\n\n開:{y.Open[-1]}\n收:{y.Close[-1]}\n高:{y.High[-1]}\n低:{y.Low[-1]}\n量:{y.Volume[-1]}\n幅:{round(((y.Close/y.Close.shift())[-1]-1)*100,2)} %",color='w',fontsize=18,bbox=dict(boxstyle='round',ec='#fa397708',fc='#fa397708'))

ax.legend(fontsize=12,loc='upper left')
ax.set_xticks(np.arange(0,len(x),len(x)/10))
ax.grid('-',alpha=.5)
ax.set_facecolor('#434343')

plt.show()
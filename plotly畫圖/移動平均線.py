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

ax.legend()

plt.show()
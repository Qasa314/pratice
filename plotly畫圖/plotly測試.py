import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go


df=pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
print(df.head())
print(df.shape)
print(df.columns)

hovertext=[]

for i in range(len(df["AAPL.Open"])):
    hl="跌"
    if df["AAPL.Close"][i]-df["AAPL.Open"][i] >0:
        hl="漲"
        
    hovertext.append("開盤價:"+str(df["AAPL.Open"][i])+"<br>"+""+
                     "收盤價:"+str(df["AAPL.Close"][i])+"<br>"+""+
                     "最高價:"+str(df["AAPL.High"][i])+"<br>"+""
                     "最低價:"+str(df["AAPL.Low"][i])+"<br>"+""+
                     hl)

    
    
    



fig=go.Figure(
    data=go.Ohlc(
    x=df["Date"],
    open=df["AAPL.Open"],
    high=df["AAPL.High"],
    low=df["AAPL.Low"],
    close=df["AAPL.Close"],
    increasing_line_color="#ff0000",
    decreasing_line_color="#00ff00",
    text=hovertext,
    hoverinfo="text"
    ))



fig.update_layout(
    title="蘋果公司股票走勢圖",  # 標題
    yaxis_title="股票價格",  # y軸名稱
    shapes = [dict(  # 顯示 ㄒ形狀的位置和線寬等資訊
        x0='2015-06-01', x1='2016-05-13',  # x的取值
        y0=0, y1=1,  # y的取值
        xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(   #  備註信息
        x='2015-06-01', y=0.05, 
        xref='x', yref='paper',
        showarrow=False, 
        xanchor='left', 
        text='下降階段')]
)

fig.show()

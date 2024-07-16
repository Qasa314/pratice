import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data1=int(input("請輸入共要查詢幾筆資料:"))
x=[]
for i in range(data1):
    m=input("請輸入想看的股票代號:(ex:2317.TW)")
    x.append(m)

sy=input("請輸入想要看的開始年:")
sm=input("請輸入想要看的開始月:")
sd=input("請輸入想要看的開始日:")
fy=input("請輸入想要看的結束年:")
fm=input("請輸入想要看的結束月:")
fd=input("請輸入想要看的結束日:")

y=sy+"-"+sm+"-"+sd
z=fy+"-"+fm+"-"+fd


df=yf.download(x,start=y,end=z)
print(df)

df.to_csv("out.csv",index=False)
df.to_excel("output.xlsx",)

df.plot(kind="line",figsize=(12,6),y=["Open","High","Low","Close"])
plt.show()

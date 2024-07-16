import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import etf

stock_list=etf.etf()
for i in range(len(stock_list)):
    stock_list[i]=stock_list[i]+".TW"
print(stock_list)


x=stock_list
df=yf.download(x,start="2020-1-1",end="2024-5-9")
df=df[["Close"]]
df=df.rename(columns={"Close":"0050"})
print(df)

df.to_excel("output.xlsx",)
"""

df.plot(kind="line",figsize=(12,6),y=["Close"])
plt.show()
"""
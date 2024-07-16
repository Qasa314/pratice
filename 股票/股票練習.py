import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
print(type(yf.Ticker))

tw2330=yf.Ticker("2330.TW")      # 台積電  

df=tw2330.history(period="max").rename(cloums={"Open":"開盤價","High":"最高價","Low":"最低價 ","Close":"收盤價" })
print(df)

plt.r
df.plot(kind="line",figsize(12,6),y=["開盤價","最高價","最低價","收盤價"])
plt.show()
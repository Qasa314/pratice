import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

x=["^TWII","^IXIC"]
df=yf.download(x,start="2020-1-1",end="2024-5-9")
print(df)

df.plot(kind="line",figsize=(12,6),y=["Open","Close"])
plt.show()
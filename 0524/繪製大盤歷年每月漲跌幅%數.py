import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

stock_id = '^TWII'
s = yf.Ticker(stock_id).history('max').Close


# 以月份來分類資料
s = s.groupby([s.index.year,s.index.month]).last().pct_change()*100

s.index.names = ['year','month']

s = s.unstack()
print(s)

fig,ax = plt.subplots(figsize=(12,10),dpi=80)
sns.heatmap(s,cmap='vlag',center=0,annot=True,fmt='.2f',ax=ax)

plt.show()

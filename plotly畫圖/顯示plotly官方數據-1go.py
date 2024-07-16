import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

stock = px.data.stocks(indexed=True) - 1  # 將原始資料減掉1
stock.head()



fig = px.bar(
  stock,  # 數據
  x=stock.index,  # x軸 
  y="GOOG"  # y軸
)

fig.show()

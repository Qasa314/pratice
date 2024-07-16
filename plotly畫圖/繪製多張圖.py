import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

stock = px.data.stocks(indexed=True) - 1  # 將原始資料減掉1
stock.head()

fig=px.area(
    stock,
    facet_col="company",#顯示不同元素的數據
    facet_col_wrap=2 ,#每列三張圖
    )


fig.show()
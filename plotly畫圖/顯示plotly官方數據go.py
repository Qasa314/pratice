import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

stocks = px.data.stocks()
stocks.head()  # 顯示前5行數據

fig=go.Figure(
    [go.Scatter(x=stocks["date"],y=stocks["FB"])]
    )





fig.update_layout(title={
    'text':'Facebook股票走勢',
    'x':0.52,
    'y':0.96,
    'xanchor':'center',
    'yanchor':'top'
})

fig.show()


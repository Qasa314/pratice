import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
fig.show()
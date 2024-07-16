import plotly.express as px
import numpy as np
import pandas as pd

df = pd.read_excel('mincpcap_cppp.xlsx')

df=df.sort_values(2024).tail(30)


fig = px.treemap(df, path=['country'], values=2024,
                  color='country',
                  title="2024平均每人每日收入/US")

fig.show()


import plotly.express as px
import numpy as np
import pandas as pd

excel_file = 'mincpcap_cppp.xlsx'  # 請替換為你的 Excel 檔案路徑
df = pd.read_excel(excel_file)

# 取得前 30 筆資料
first_30_rows = df.head(30)

df = first_30_rows
df["world"] = "world"  # in order to have a single root node
fig = px.treemap(df, path=['world', 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.show()
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用

df_data = px.data.iris()
fig = px.histogram(df_data, x="sepal_width",color="species")
fig.update_layout(barmode="overlay")  #圖案重疊
fig.update_traces(opacity=0.75)		#透明度

fig.write_html('figure.html', auto_open=True)  #產生網頁並自動開啟瀏覽器預覽


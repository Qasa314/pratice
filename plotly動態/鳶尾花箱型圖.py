import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用

df_data = px.data.iris()
print(df_data)
fig = px.box(df_data, y="sepal_width")
fig.show()

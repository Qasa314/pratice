import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用

df_data = px.data.iris()
print(df_data)
fig = px.scatter_3d(df_data, x="sepal_width", y="sepal_length", z="petal_width",color="species",size='petal_length')
fig.show()



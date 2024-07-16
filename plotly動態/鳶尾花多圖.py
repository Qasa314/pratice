import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用

df_data = px.data.iris()
print(df_data)
fig = px.scatter_matrix(df_data, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
fig.show()
HTML(fig.to_html())
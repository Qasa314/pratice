import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用

df_data = px.data.iris()
print(df_data)
fig = px.scatter(df_data, x="sepal_width", y="sepal_length",color="species",hover_data=['petal_length','petal_width'])
fig.show()
HTML(fig.to_html())	#jupyter專用


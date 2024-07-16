import plotly.express as px
import plotly.graph_objects as go
from IPython.display import HTML  #jupyter專用
import kaleido
df_data = px.data.iris()
print(df_data)
fig = px.scatter(df_data, x="sepal_width", y="sepal_length", color="species", marginal_y="histogram", marginal_x="histogram", trendline="ols", template="simple_white")

fig.write_image("demo.png")
fig.show()

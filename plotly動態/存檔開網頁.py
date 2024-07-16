import plotly.express as px
from IPython.display import HTML  #jupyter專用


fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

#三種顯示方式 依照開發工具選擇
fig.show() #標準輸出會自動開啟網頁,線上開發工具無法使用
HTML(fig.to_html()) #jupyter專用,先輸出成網頁檔案再顯示
fig.write_html('figure.html', auto_open=True)  #產生網頁並自動開啟瀏覽器預覽

import folium

# 在一個列表中儲存緯度、經度和地點的名稱*
lats = ["25.0518341"]
lons = ["121.5441847"]
names = ["恆逸教育訓練中心"]

# 用一個初始位置建立一個地圖*
m = folium.Map(location=[lats[0], lons[0]], zoom_start=16)
 # 建立地圖與設定位置

for lat, lon, name in zip(lats, lons, names):
  # 用其他位置建立標記*
  folium.Marker(
    location=[lat, lon], popup=name, icon=folium.Icon(color="green")
  ).add_to(m)


m.save('map.html')

import seaborn as seaborn
import matplotlib.pyplot as plt
import numpy as np

mean = 3
number = 50

x1 = np.random.normal(mean, 1, size=number)
y1 = np.random.normal(mean, 1, size=number)
z1 = np.random.normal(mean, 1, size=number)
s1 = np.random.normal(mean, 1, size=number)*50

print(x1,y1,z1)
plt.figure(figsize=(6, 5))
axes = plt.axes(projection="3d") #axes() 函式建立一組軸 projection 關鍵字並將 3D 值作為字串傳遞
print(type(axes)) #檢查 axes 的型別，我們將看到這些是 3D 子圖軸

axes.scatter3D(x1, y1, z1, s=s1)

axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
plt.show()

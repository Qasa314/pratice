import numpy as np
import matplotlib.pyplot as plt

start = 0
end = np.pi * 20   
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x) 

# 取得 mpl_toolkits.mplot3d.axes3d.Axes3D 實例
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter3D(x, y, z,s=1,c=x)		#scatter3D
plt.title('Axes3D Plot')
plt.show()
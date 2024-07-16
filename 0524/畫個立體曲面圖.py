import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def f(x, y):
    n = np.sqrt(np.power(x, 2) + np.power(y, 2)) / 180 * np.pi
    return np.cos(n) + np.cos(3 * n)

width = 200
step = 10

x = np.arange(-width, width, step)
y = np.arange(-width, width, step)

X, Y = np.meshgrid(x, y) 
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm) 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((1, 1, 0.5))
plt.title('Axes3D Plot Surface')
plt.show()
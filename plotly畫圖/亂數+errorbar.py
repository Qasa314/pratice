import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
mynum=np.linspace(-10,10,50)
x=mynum
y=np.random.randint(-10,10,50)
fig = plt.figure()  # 宣告畫布
plt.errorbar(x, y, yerr=2, fmt='o',color="SteelBlue",ecolor="LightBlue",elinewidth=2)  # 畫圖
plt.title("")
plt.show #顯示
fig.savefig("errorbar.png") #存檔
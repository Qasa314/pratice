import numpy as np
import matplotlib.pyplot as plt

mynum=np.linspace(-10,10,100)
x=mynum
y=np.sin(mynum)
fig=plt.figure() #宣告畫布
plt.plot(x,y,".",x,np.cos(mynum),"--") #畫圖
plt.show #顯示
fig.savefig("day15_01.png") #存檔

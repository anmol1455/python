import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
a=np.linspace(0,1,100)
x=a*np.sin(a+25)
y=a*np.cos(a*25)
x1=a*np.sin(a*15)
y1=a*np.cos(a+15)
fig=plt.figure()
ax=plt.axes(projection="3d")
z=x1+y1
ax.plot3D(a,x,y,"r")
ax.scatter3D(a,x1,y1,"r",c=z)
plt.show()

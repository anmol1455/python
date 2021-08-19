import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
plt.plot(x,np.sin(x),"y--")
plt.plot(x,np.cos(x),"r*")
plt.plot(x,np.tan(x),"g^")
plt.title("graph")
plt.xlabel("number")
plt.ylabel("angle value")
plt.show()

import numpy as np
from matplotlib import *
import matplotlib.pyplot as plt
x=np.array(["a","b","c","d","e"])
y=np.array([40,45,42,38,29])
z=np.array([45,25,43,28,37])
a=np.array([46,23,26,40,41])
b=np.array([45,25,42,33,36])
f,n=plt.subplots(2,2)
n[0][0].plot(x,y,"r")
n[0][0].set_title("english")
n[0][1].plot(x,z,"g")
n[0][1].set_title("hindi")
n[1][0].plot(x,a,"o")
n[1][0].set_title("math")
n[1][1].plot(x,y,"b")
n[1][1].set_title("computer")
plt.show()

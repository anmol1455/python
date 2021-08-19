import matplotlib.pyplot as plt
import random as r
import numpy as np
a=np.arange(0,50,1)
li=[]
for i in np.random.randn(50):
    li.append(i)
print(li)
b=np.array(li)
fig=plt.figure()
fig.add_axes([.1,.2,.5,.5])
plt.hist(b,color='g',bins=20)
plt.scatter(b,a,color="r")
plt.show()

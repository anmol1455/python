import numpy as np

a=np.arange(25)
a.shape=(5,5)
print(a)
for i in np.nditer(a):
          print(i)
b=np.copy(a.T)
print(b)
b=b*2
for i in np.nditer(b):
          print(i)
print(a)

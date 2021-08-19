import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import ExcelFile
d=pd.read_excel("data.xlsx","Sheet1")
print(d)
x=d['Item']
y=d['Units']
z=d['UnitCost']
a=d['Total']
plt.plot(x,y,'r')
fig=plt.figure()
fig.add_axes([0.1,0.1,0.5,0.5])
n=fig.subplots(2,2)
n[0][0].bar(x,y,color='b',width=.25)
n[0][1].bar(x,z,color='g',width=.25)
n[1][0].bar(x,a,color='r',width=.25)
n[1][1].bar(x,z,color='b',width=.25)
plt.show()

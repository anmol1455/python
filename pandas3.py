import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
arr=np.array([10,20,30,40])
arr1=np.array([100,200,300,400])
data=pd.Series(arr,index=[1,2,3,4])
print(data)
data1=pd.Series(arr1,index=[1,2,3,4])
ndata=pd.DataFrame([arr,arr1],columns=['hindi','english','maths','science'],index=[1,2])
print(ndata)
plt.plot(ndata['hindi'],ndata['english'])
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.5,0.5])
ax.bar(data.index+0.00,data,color="orange",width=0.25)
ax.bar(data.index+0.25,data,color="red",width=0.25)
plt.show()


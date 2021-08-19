import pandas as pd
import numpy as np
details=[['anmol',90,99],['aradhya',52,65],['abhi',45,90]]
data=pd.DataFrame(details,columns=['name','english','hindi'],index=[1,2,3])
data['math']=[98,45,78]
data['total']=data['english']+data['hindi']+data['math']
data['per']=data['total']/3
d=[]
for i in data['per']:
    if(i>90):
        d.append('A')
    elif(i>80):
        d.append('B')
    else:
        d.append('C')
data['div']=d
print(data)
print(data.loc[1])
d=[{'a':10,'b':80},{'b':50,'c':100}]
df=pd.DataFrame(d)
print(df)

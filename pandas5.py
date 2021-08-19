import pandas as pd
import numpy as np
d=[{'a':10,'b':20},{'b':50,'c':100},{'a':10,'b':20,'c':30},{}]
df=pd.DataFrame(d)
df['d']=[np.nan,np.nan,np.nan,np.nan]
print(df)
#df=df.fillna(0.00)
#df=df.fillna(method='pad')
#df=df.fillna(method='bfill')
#df=df.dropna(how='all')
#df=df.dropna(how='any')by default for rows
#df=df.dropna(how='all',axis='columns')
df=df.replace(10,value=50,inplace=False)#replace 10 by 50
print(df)

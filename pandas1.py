import pandas as pd
import numpy as np
name=pd.Series(['Anmol','Akhand','Abhinav'],index=['a','b','c'])#index will as 0 1 2 if we dont specify the index
print(name)
print(name['a'])
print(name['a':'b'])
stud=['ram','sita','lakhan','bharat']
marks=[50,60,45,58]
details=pd.Series(marks,index=stud)
print(details)
population={'dilli':2500000,'up':5200000,'bihar':4500000}
p=pd.Series(population)
print(p)
print(p.index)
print(p.values)
arr=np.array(np.random.rand(3,2))
print(arr)
area={'dilli':230000,'up':58500,'bihar':89000}
pa=pd.Series(area)
ndata=pd.DataFrame(arr,index=['a','b','c'],columns=['first','second'])
adata=pd.DataFrame([population,area],index=['population','area'])
print(ndata)
print(adata)
print(adata['dilli'])
density=pd.DataFrame([p.index,p.values/pa.values],index=['city','density'])
print(density)
andata=pd.DataFrame([area,population],index=['area','population'])
print(type(ndata))
anndata=pd.DataFrame(andata.transpose(),columns=['area','population'])
print(anndata['population']/anndata['area'])

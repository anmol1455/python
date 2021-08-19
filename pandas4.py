import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
population={1:28900,2:63465,3:75273,4:62467}
area={1:4564,2:7432,3:5643,4:8633}
ndata=pd.DataFrame([population,area],index=['population','area'])
print(ndata)
a=ndata.loc['population']
b=ndata.loc['area']
print(a,"\n",b)
plt.bar(ndata.columns+0.00,a,width=0.25)
plt.bar(ndata.columns+0.25,b,width=0.25)
plt.legend(['area','population'])
plt.show()

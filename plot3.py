import numpy as np
import matplotlib.pyplot as plt
sales=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
#city=np.array(["vns","mrt","gzp","sln"])
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.5,0.5])
'''sales=np.array([10,20,30,40])
ax.pie(sales,labels=city,autopct="%1.3f%%")
ax.set_title("Sales report")'''
city=np.array([1,2,3,4])
ax.bar(city+0.00,sales[0],color="orange",width=0.25)
ax.bar(city+0.25,sales[1],color="red",width=0.25)
ax.bar(city+0.50,sales[2],color="green",width=0.25)
ax.legend(["mouse","cpu","monitor"])
ax.set_title("Sales report")

plt.show()

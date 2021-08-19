import mysql.connector as back
import numpy as np
import matplotlib.pyplot as plt
mydb=back.connect(host="localhost",user="root",passwd="",database="mydata")
cur=mydb.cursor()
cur.execute("select name from student")
result=cur.fetchall()
arr_name=np.array([result]).ravel()
print(arr_name)
cur.execute("select english from student")
result1=cur.fetchall()
arr_eng=np.array([result1]).ravel()
print(arr_eng)
cur.execute("select hindi from student")
result2=cur.fetchall()
arr_hin=np.array([result2]).ravel()
print(arr_hin)
cur.execute("select maths from student")
result3=cur.fetchall()
arr_math=np.array([result3]).ravel()
print(arr_math)
cur.execute("select gk from student")
result4=cur.fetchall()
arr_gk=np.array([result4]).ravel()
print(arr_gk)
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.5,0.5])
ax.bar(arr_eng+.00,arr_name,width=0.30)
ax.bar(arr_hin+.30,arr_name,width=0.30)
ax.bar(arr_math+.60,arr_name,width=0.30)
plt.show()


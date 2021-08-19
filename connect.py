import mysql.connector as back
import numpy as np
mydb=back.connect(host="localhost",user="root",passwd="",database="mydata")
cur=mydb.cursor()
cur.execute("select * from student")
result=cur.fetchall()
for i in result:
         print(i)
mydb.commit()


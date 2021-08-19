import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="collage")
cur=myconn.cursor()
cur.execute("select * from student")
for i in cur:
    print(i)

myconn.close()

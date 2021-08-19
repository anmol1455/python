import mysql.connector
Sname=input("enter student name")
collage=input("enter collage name")
myconn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="collage")
cur=myconn.cursor()
try:
    cur.execute("insert into student(Sname,collage)values('%s','%s')"%(Sname,collage))
    myconn.commit()
except:
    myconn.rollback()
print(cur.rowcount,"record inserted")
myconn.close()

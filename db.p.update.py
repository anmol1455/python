import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
cur=conn.cursor()

stid=input("enter student id: ")
#stname=input("enter student name: ")
stroll=int(input("enter student roll number: "))
stclass=int(input("enter student class: "))
#stadd=input("enter student address: ")

try:
    cur.execute("update studentdetails set rollno=%d,stdclass=%d where sid='%s'"%(stroll,stclass,stid))
    conn.commit()
except:
    conn.rollback()
print(cur.rowcount,"student detail inserted")







conn.close()

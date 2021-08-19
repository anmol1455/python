import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
cur=conn.cursor()
#cur.execute("create database studreport")
#cur.execute("show databases")
#for x in cur:
 #   print(x)
#cur.execute ("create table studentdetails(sid varchar(100) primary key,sname varchar(200) not null,rollno int not null,stdclass int not null,address varchar(400) not null)")
#cur.execute("show tables")
#for x in cur:
#    print(x)
stid=input("enter student id: ")
stname=input("enter student name: ")
stroll=int(input("enter student roll number: "))
stclass=int(input("enter student class: "))
stadd=input("enter student address: ")
try:
    cur.execute("insert into studentdetails(sid,sname,rollno,stdclass,address)values('%s','%s',%d,%d,'%s')"%(stid,stname,stroll,stclass,stadd))
    conn.commit()
except:
    conn.rollback()
print(cur.rowcount,"student detail inserted")
conn.close()

import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
cur=conn.cursor()
#cur.execute("create database studreport")
#cur.execute("show databases")
#for x in cur:
 #   print(x)
#cur.execute ("create table studentdetails(sid varchar(100) primary key,sname varchar(200) not null,rollno int not null,stdclass int not null,address varchar(400) not null)")

cur.execute("create table Reportcard(reportid varchar(200) primary key, sid varchar(100), examtype varchar(200) not null, session varchar(300) not null, hindi int not null, english int not null, math int not null, science int not null, s_st int not null, total int not null, percentage int not null, grade varchar(100) not null, status varchar(100) not null, foreign key(sid) references studentdetails(sid))")
            












cur.execute("show tables")
for x in cur:
    print(x)
conn.close()

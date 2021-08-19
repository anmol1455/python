import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="jobs")
cur=conn.cursor()
#cur.execute("create databases jobs")
#cur.execute("show databases")
#for x in cur:
  #  print(x)
#cur.execute('create table vacancies(sno varchar(100) primary key,post varchar(500)not null,vacancy int not null)')
s_no=input("enter serial number")
posts=input("enter post")
vac=int(input("enter number of vacancies"))
try:
    cur.execute("insert into vacancies(sno,post,vacancy)values('%s','%s',%d)"%(s_no,posts,vac))
  
    conn.commit()
except:
    conn.rollback()
print(cur.rowcount,"record inserted")
        
conn.close()

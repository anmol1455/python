import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
cur=conn.cursor()
reptid=input("enter report id: ")
stid=input("enter student id: ")
examty=input("enter examtype: ")
sess=input("enter session: ")
hin=int(input("enter hindi marks: "))
eng=int(input("enter english marks: "))
mat=int(input("enter maths marks: "))
sci=int(input("enter science marks: "))
sst=int(input("enter s.st marks: "))
tot=int(input("enter total marks: "))
per=int(input("enter percentage: "))
gra=input("enter grade: ")
stat=input("enter status: ")


try:
    cur.execute("insert into Reportcard(reportid,sid,examtype,session,hindi,english,math,science,s_st,total,percentage,grade,status)values('%s','%s','%s','%s',%d,%d,%d,%d,%d,%d,%d,'%s','%s')"%(reptid,stid,examty,sess,hin,eng,mat,sci,sst,tot,per,gra,stat))
    conn.commit()
except:
    conn.rollback()
print(cur.rowcount,"student detail inserted")
conn.close()

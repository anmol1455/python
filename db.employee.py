import mysql.connector
conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="employeedata")
cur=conn.cursor()
#cur.execute("create table employee(empid int auto_increment primary key,empname varchar(100)not null,salary int not null,designation varchar(500) not null)")
#cur.execute("show tables")
#for x in cur:
#    print(x)
try:
    insert=("insert into employee(`empid`,`empname`,`salary`,`designation`)values(%d,'%s',%d,'%s')")
    val=[('ankit',5000,'labour'),
         ('raj',25000,'manager')]
    cur.execute(insert,val)
    conn.commit()
except:
    conn.rollback()
print(cur.rowcount,"record inserted")
conn.close()

import mysql.connector as db
mydb=db.connect(host='localhost',user='root',passwd='',database='mydata')
cur=mydb.cursor()
#cur.execute("show tables")
#for i in cur:
#    print (i)
#cur.execute("CREATE TABLE student(rollno int PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20))")
sql="insert into student(rollno,name)values(%s,%s)"
val=[(102,'Shyam Singh'),(103,'Abhinav Singh'),(104,'Akhand Pratap Singh')]
cur.executemany(sql,val)
mydb.commit()

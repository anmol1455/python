import mysql.connector as db
mydb=db.connect(host='localhost',user='root',passwd='',database='mydata')
cur=mydb.cursor()
cur.execute("show databases")
for i in cur:
    print (i)

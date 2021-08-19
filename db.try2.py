class connection:
    def connects():
        
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
        cur=conn.cursor()
        conn.close()

        stid=""
        stname=""
        stroll=0
        stclass=0
        stadd=""
    def inputdata():
        self.stid=input("enter student id: ")
        self.stname=input("enter student name: ")
        self.stroll=int(input("enter student roll number: "))
        self.stclass=int(input("enter student class: "))
        self.stadd=input("enter student address: ")

class insertion(connection):
    
    def insert(self):
        self.cur=conn.cursor()
        try:
            self.cur.execute("insert into studentdetails(sid,sname,rollno,stdclass,address)values('%s','%s',%d,%d,'%s')"%(self.stid,self.stname,self.stroll,self.stclass,self.stadd))
            self.conn.commit()
        except:
            self.conn.rollback()
        print(cur.rowcount,"student detail inserted")





inputss=insertion()
inputss.connect()
print("input detail for insertion")
inputss.inputdata()
inputss.insert()

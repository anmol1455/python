class connection:
    def connect(self):
        conn=""
        cur=""
        import mysql.connector
        self.conn=mysql.connector.connect(host="localhost",user="jarvis",passwd="1408",database="studreport")
        self.cur=self.conn.cursor()
        stid=""
        stname=""
        stroll=0
        stclass=0
        stadd=""
    def inputdata(self):
        self.stid=input("enter student id: ")
        self.stname=input("enter student name: ")
        self.stroll=int(input("enter student roll number: "))
        self.stclass=int(input("enter student class: "))
        self.stadd=input("enter student address: ")

    def updinputdata(self):
        self.stid=input("enter student id: ")
        self.stroll=int(input("enter student roll number: "))
        self.stclass=int(input("enter student class: "))

class insertion(connection):
    
    def insert(self):
        self.cur=self.conn.cursor()
        try:
            self.cur.execute("insert into studentdetails(sid,sname,rollno,stdclass,address)values('%s','%s',%d,%d,'%s')"%(self.stid,self.stname,self.stroll,self.stclass,self.stadd))
            self.conn.commit()
        except:
            self.conn.rollback()
        print(self.cur.rowcount,"student detail inserted")
        self.conn.close()

class updation(connection):
    
    def update(self):
        self.cur=self.conn.cursor()

        try:
            self.cur.execute("update studentdetails set rollno=%d,stdclass=%d where sid='%s'"%(self.stroll,self.stclass,self.stid))
            self.conn.commit()
        except:
            self.conn.rollback()
        print(self.cur.rowcount,"student detail updated")
        self.conn.close()



print("whant you want to do")
print("press 1 for insert")
print("press 2 for update")
num=int(input())
if(num==1):
    inputs=insertion()
    inputs.connect()
    print("input detail for insertion")
    inputs.inputdata()
    inputs.insert()
elif(num==2):
    modify=updation()
    modify.connect()
    print("input detail for updation")
    modify.updinputdata()
    modify.update()
else:
    print("choose correct option")


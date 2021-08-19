import tkinter
from tkinter import messagebox
import mysql.connector as back


myform=tkinter.Tk(className="Add")
name=tkinter.Label(text="Roll")
Add=tkinter.Label(text="Course",bg="Red",fg="white")
name.grid(row=0)
Add.grid(row=1)
nm=tkinter.Entry()
ad=tkinter.Entry()
nm.grid(row=0,column=1)
ad.grid(row=1,column=1)
def store():
          mydb=back.connect(host="localhost",user="root",passwd="",database="mydata")
          cur=mydb.cursor()
          roll=nm.get()
          cur.execute("select course from student where Roll="+roll)
          res=cur.fetchone()
          print(res)
          ad.insert(0,res[0])
          messagebox.showinfo("output",("store succesfully"))
save=tkinter.Button(text="Save",width="20",command=store)
save.grid(row=5,column=1)

myform.mainloop()


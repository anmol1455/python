import tkinter
from tkinter import messagebox
import mysql.connector as back


myform=tkinter.Tk(className="Add")
name=tkinter.Label(text="Name")
Add=tkinter.Label(text="Address",bg="Red",fg="white")
name.grid(row=0)
Add.grid(row=1)
nm=tkinter.Entry()
ad=tkinter.Entry()
nm.grid(row=0,column=1)
ad.grid(row=1,column=1)
def store():
          mydb=back.connect(host="localhost",user="root",passwd="",database="mydata")
          cur=mydb.cursor()
          name=nm.get()
          add=ad.get()
          sql="insert into student(name,course)values(%s,%s)"
          val=(name,add)
          cur.execute(sql,val)
          mydb.commit()
          messagebox.showinfo("output",("store succesfully"))
save=tkinter.Button(text="Save",width="20",command=store)
save.grid(row=5,column=1)

myform.mainloop()


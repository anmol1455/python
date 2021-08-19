import tkinter
from tkinter import *
myform=tkinter.Tk(className="Add")
name=tkinter.Label(text="Name")
Add=tkinter.Label(text="Address",bg="Red",fg="white")
name.grid(row=0)
Add.grid(row=1)
nm=tkinter.Entry()
ad=tkinter.Entry()
nm.grid(row=0,column=1)
ad.grid(row=1,column=1)
multy=tkinter.Text()
multy.grid(row=4,column=0)
def store():
          name=nm.get()
          add=ad.get()
          file=open("mydata.txt","a")
          file.write(name+"\t"+add+"\n")
          file.close()
          messagebox.showinfo("output",("Succesfully save"))
def read():
          file=open("mydata.txt","r")
          data=file.read()
          multy.insert('1.0',data)
          
          
save=tkinter.Button(text="Save",width="20",command=store)
save.grid(row=5,column=1)
show=tkinter.Button(text="show",width="20",command=read)
show.grid(row=5,column=0)
myform.mainloop()


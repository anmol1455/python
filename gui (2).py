import tkinter
from tkinter import messagebox
myform=tkinter.Tk(className="File")
name=tkinter.Label(text="Name")
name.grid(row=0)
Address=tkinter.Label(text="Address",bg="green",fg="red")
Address.grid(row=1)
nme=tkinter.Entry()
nme.grid(row=0,column=1)
add=tkinter.Entry()
add.grid(row=1,column=1)
data=tkinter.Text()
data.grid(row=2,column=1)
def store():
    name=nme.get()
    Address=add.get()
    file=open("anm.txt",'a')
    file.write("Name="+name+"\t"+"Address="+Address)
    file.close()
    messagebox.showinfo("output",("file successfully written"))
def read():
    file=open("anm.txt",'r')
    text=file.read()
    data.insert('1.0',text)
read=tkinter.Button(text="read the file",width="20",command=read)
save=tkinter.Button(text="write to file",width="20",command=store)
save.grid(row=2,column=2)
read.grid(row=2,column=3)
myform.mainloop()    

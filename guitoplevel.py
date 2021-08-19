import tkinter as tk
from tkinter import messagebox 
def file():
    f=tk.Toplevel()
    l=tk.Label(f,text="I'm file window")
    b=tk.Button(f,text="File",command=msg)
    b.grid(row=0,column=1)
    l.grid(row=1,column=4)
def edit():
    f=tk.Toplevel()
    l=tk.Label(f,text="This is edit window")
    l.pack()
def view():
    f=tk.Toplevel()
    l=tk.Label(f,text="This is view window")
    l.pack()
def msg():
    messagebox.showinfo("output","Hello System")
frame=tk.Tk(className="Form")
c=tk.PanedWindow(frame)
j=tk.Label(c,text="My name is System")
j.grid(row=4,column=2)
c.grid(row=2,column=1)
b1=tk.Button(frame,text="File",command=file)
b1.grid(row=0,column=1)
b2=tk.Button(frame,text="Edit",command=edit)
b2.grid(row=0,column=2)
b1=tk.Button(frame,text="View",command=view)
b1.grid(row=0,column=3)
frame.mainloop()


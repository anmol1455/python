import tkinter
from tkinter import ttk
from tkinter import messagebox
form=tkinter.Tk()
v=tkinter.IntVar()
def fun():
    name=str(v.get())
    messagebox.showinfo("something",name)
male=tkinter.Radiobutton(form,text="Male",value=1,variable=v,command=fun)
female=tkinter.Radiobutton(form,text="female",value=2,variable=v,command=fun)
male.grid(row=1)
female.grid(row=2)
fruits=tkinter.Listbox(form)
fruits.insert("0","apple")
fruits.insert("1","orange")
fruits.insert("2","banana")
fruits.insert("3","mango")
fruits.insert("4","grapes")
def fun1():
    messagebox.showinfo("something",fruits.get(fruits.curselection()))
show=tkinter.Button(form,text="show",command=fun1)
fruits.grid(row=3)
show.grid(row=4)
def fun2():
    messagebox.showinfo("msg",city.get())
city=ttk.Combobox(form)
city['values']=('vns','lkh','hdrbd','knp')
val=tkinter.Button(form,text="show value",command=fun2)
def fun3(e):
    messagebox.showinfo("msg",fruit.get())
fruit=ttk.Combobox(form)
fruit['values']=('apple','orange','banana','mango')
fruit.bind("<<ComboboxSelected>>",fun3)
fruit.grid(row=5,column=2)
city.grid(row=5)
val.grid(row=6)
def fun4():
    c=str(val.get())
    messagebox.showinfo("scale",str(c))
val=tkinter.IntVar()
s=tkinter.Scale(form,variable=val)
s.grid(row=7)
vals=tkinter.Button(form,text="show scale value",command=fun4)
vals.grid(row=8)

form.mainloop()

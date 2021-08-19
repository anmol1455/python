import tkinter
from tkinter import messagebox
form=tkinter.Tk(className="Gui with oop")
name=tkinter.Entry(form)
name.grid(row=1)
class A:
    def add(self,t):
        n=name.get()
        messagebox.showinfo("notice",("hello" +n+ " "+t))
obj=A()
btn=tkinter.Button(form,text="click me",command=lambda:obj.add("Singh"))
btn.grid(row=2)
form.mainloop()

import tkinter as t
form=t.Tk()
scroll=t.Scrollbar(form)
scroll.pack(side="right",fill="y")
list=t.Listbox(form,yscrollcommand=scroll.set)
c=0
for i in range(100):
    list.insert(c,i)
    c+=1
list.pack(side="left",fill="both")
scroll.config(command=list.yview)
form.mainloop()

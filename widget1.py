import tkinter
form=tkinter.Tk(className="widget")
scroll=tkinter.Scrollbar(form)
scroll.pack(side="right",fill="y")
#scroll.grid(row=9)
list=tkinter.Listbox(form,yscrollcommand=scroll.set)
c=0
for i in range(100):
    list.insert(c,i)
    c+=1
list.pack(side="left",fill="both")
scroll.config(command=list.yview)
form.mainloop()

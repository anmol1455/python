from tkinter import *
root = Tk()

height = 3
width = 5

delta=0

entries = []

for i in range(height): #Rows
  newrow = []
  for j in range(width): #Columns
    b = Entry(root, text="",width=8)
    b.grid(row=i, column=j)
    newrow.append(b)
  entries.append(newrow)

mainloop()

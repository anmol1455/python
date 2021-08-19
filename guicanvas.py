import tkinter as tk
from tkinter.ttk import *
frame=tk.Tk()
frame.geometry('1500x1500')
c=tk.Canvas(frame,bg="white",height=1300,width=1000)
'''c.create_line(100,50,500,50)#horizontal
c.create_line(100,100,100,25)#vetical
c.create_oval(20,20,200,200,outline="green")#circle
c.create_oval(20,20,200,100,outline="blue",fill="red")#oval
c.create_rectangle(10,10,100,60,outline="blue")
c.create_arc(20,150,125,30,fill="green")'''
c.create_polygon(100,200,300,400,500,450,270,380,outline="black",fill="cyan")
c.create_text(100,150,text="hey there")
im=tk.PhotoImage(file=r"C:\Users\hp\Pictures\Camera Roll\WIN_20201007_11_16_53_Pro.jpg")
c.create_image(500,500,image=im)
c.pack()
frame.mainloop()

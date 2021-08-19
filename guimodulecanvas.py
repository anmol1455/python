import tkinter as tk
from tkinter.ttk import *
def f():
    frame=tk.Tk()
    frame.geometry('1500x1500')
    c=tk.Canvas(frame,bg="white",height=1300,width=1200)
    return c,frame
def circle():
    c,e=f()
    c.create_oval(20,20,200,200,outline="red")
    c.pack()
    e.mainloop()
def rect():
    c,e=f()
    c.create_rectangle(10,10,100,60,outline="red")
    c.pack()
    e.mainloop()
def oval():
    c,e=f()
    c.create_oval(20,20,200,100,outline="red")
    c.pack()
    e.mainloop()
def hline():
    c,e=f()
    c.create_line(100,50,500,50)
    c.pack()
    e.mainloop()
def vline():
    c,e=f()
    c.create_line(100,100,100,50)
    c.pack()
    e.mainloop()
def arc():
    c,e=f()
    c.create_arc(20,150,125,30,fill="blue")
    c.pack()
    e.mainloop()
def poly():
    c,e=f()
    c.create_polygon(20,150,125,30,70,500,fill="blue")
    c.pack()
    e.mainloop()
def text():
    c,e=f()
    c.create_text(200,150,text="hello")
    c.pack()
    e.mainloop()
def image():
    c,e=f()
    im=tk.PhotoImage(file=r"C:\Users\hp\Pictures\Camera Roll\WIN_20201007_11_16_53_Pro.jpg")
    c.create_image(500,500,image=im)
    c.pack()
    e.mainloop()














    
    








    
    

import tkinter as tk
from tkinter import messagebox
frame=tk.Tk()
frame.geometry('500x500')
lf=tk.LabelFrame(frame,text="this is LabelFrame",height=100,width=150)
l=tk.Label(lf,text="Label inside LabelFrame")
l.grid(row=0,column=0)
lf.grid(row=0,column=0)
frame.mainloop()

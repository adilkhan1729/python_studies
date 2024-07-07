# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# window=tk.Tk()

# def submit():
#   d2=check.get()
#   print("chatbox",d2)
#   messagebox.showwarning("warning","button clicked")

# window.geometry=("400x400")  
# window.title("id")
# frame=Frame(window,bd=5,bg="green").pack()
# name=Label(frame,text="name").place(x=20,y=140)
# name_entry=Entry(frame).place(x=100,y=140)
# id=Label(frame,text="id").place(x=20,y=200)
# id_entry=Entry(frame).place(x=100,y=200)
# submit=Button(frame,text="submit",activebackground="purple").place(x=50,y=250)
# check=Checkbutton(window,text="testcheckbutton",onvalue=0,offvalue=1,height=4,width=26).place(x=5,y=60)

# window.mainloop()

from tkinter import *
window=Tk()
window.geometry("150x150")
frame=Frame(window)
frame.pack()
topframe=Frame(window)
topframe.pack(side=LEFT)
bottomframe=Frame(window)
bottomframe.pack(side=RIGHT)

name1=Label(frame,text="label1").pack(side=RIGHT)
name2=Label(topframe,text="label2").pack(side=RIGHT)
name3=Label(topframe,text="label3").pack(side=RIGHT)
name4=Label(bottomframe,text="label4").pack(side=LEFT)

window.mainloop()
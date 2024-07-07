import tkinter
from tkinter import *
window= tkinter.Tk()
window.title("reception")
var3=StringVar()
var2=StringVar()
var1=StringVar()
window.geometry("400x200")
def test ():
    name_data=var1.get()
    name=var2.get()
    password=var3.get()
    print(password)
    print(name)
    print(name_data)

    
l1=Label(window,text="name").place(x=10,y=5)
l2=Label(window,text="last_name").place(x=10,y=30)
l3=Label(window,text="password").place(x=10,y=55)
l12=Entry(window,textvariable=var1).place(x=80,y=10)
l121=Entry(window,textvariable=var2).place(x=80,y=30)
l122=Entry(window,textvariable=var1).place(x=80,y=55)
b=Button(window,text="submit",bg="red",command=test).place(x=10,y=75)
Checkbutton
window.mainloop()

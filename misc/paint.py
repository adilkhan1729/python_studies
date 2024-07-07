from functools import partial
from tkinter import *
from  tkinter import Canvas
root=Tk()
root.title("paint application")
root.geometry("1000x500")
colour="blue"
strokesizevar=IntVar()
strokesizevar.set(20)

frame1=Frame(root,bg="yellow",relief="sunken",borderwidth=5)
frame1.pack(side=LEFT,fill=Y)
frame2=Frame(root,bg="white",relief="raised",borderwidth=5)
frame2.pack(side=RIGHT,fill=Y)

def draw(event):
    x1=event.x
    y1=event.y
    x2=x1+strokesizevar.get()
    y2=y1+strokesizevar.get()

    drawBoard.create_polygon(x1,y1,x2,y2,fill=colour,outline=colour)
drawBoard=Canvas(frame2,height=600,width=750 ,bg="purple")    
drawBoard.pack()
drawBoard.bind("<B1-Motion>",draw)   
root.mainloop() 












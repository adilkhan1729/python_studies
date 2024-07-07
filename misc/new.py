import tkinter
top= tkinter.Tk()
Can=tkinter.Canvas(top,bg="red",height=500,width=500)
imagename=tkinter.PhotoImage(file="abc1.png")
image=Can.create_image(300,300,image=imagename)
coord=100,100,300,200
arc=Can.create_oval(200,100,300,200,fill="grey")
Can.pack(fill=tkinter.BOTH,expand=1)
top.mainloop()
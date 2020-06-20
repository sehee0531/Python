from tkinter import *

top = Tk()

cnvs=Canvas(top,width=300,height=200)

cnvs.pack()

cnvs.create_arc(10,10,200,150,extent=90,style=PIESLICE)

top.mainloop()
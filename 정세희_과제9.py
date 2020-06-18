from tkinter import *

w=Tk()
w.title("라디오버튼과 체크버튼")


def circle():
    cnvs.create_oval(10,10,200,150,fill=fillColor)
    

def rectangle():
    cnvs.create_rectangle(10,10,200,150,fill=fillColor)
    

def line():
    cnvs.create_line(10,10,200,150)
    

def color():
    global fillColor, fillVar
    if fillVar.get()==1:
        fillColor="pink"
    else:
        fillColor=None
    

cnvs=Canvas(w,width=300,height=200)
cnvs.pack()

v=IntVar()
fillVar=IntVar()
fillColor=None

rb1=Radiobutton(w,text="직사각형", variable=v,
                value='직사각형', command=rectangle)
rb2=Radiobutton(w,text="타 원", variable=v,
                value='타 원', command=circle)
rb3=Radiobutton(w,text="직 선" ,variable=v,
                value='직 선', command=line)
cb1=Checkbutton(w,text="색채우기", variable=fillVar,command=color)

rb1.pack(side=LEFT,padx=10,anchor=W)
rb2.pack(side=LEFT,padx=10,anchor=W)
rb3.pack(side=LEFT,padx=10,anchor=W)
cb1.pack(side=LEFT,padx=10,anchor=W)


w.mainloop()   
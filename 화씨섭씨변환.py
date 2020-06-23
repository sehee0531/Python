from tkinter import *

top=Tk()

def p():
    cvt=float(en1.get())
    cvt=(cvt-32)*5/9
    en2.insert(0,cvt)

def c():
    cmt=float(en2.get())
    cmt=cmt*9/5+32
    en1.insert(0,cmt)


lb1=Label(top,text="화씨")
en1=Entry(top)
lb2=Label(top,text="섭씨")
en2=Entry(top)
bt1=Button(top,text="화씨->섭씨",command=p)
bt2=Button(top,text="섭씨->화씨",command=c)
lb1.grid(row=0,column=0)
en1.grid(row=0,column=2)
lb2.grid(row=1,column=0)
en2.grid(row=1,column=2)
bt1.grid(row=2,column=0)
bt2.grid(row=2,column=2)

top.mainloop()
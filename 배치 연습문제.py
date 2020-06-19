from tkinter import *

top=Tk()

Button(top,text="위쪽",width=10).pack(side=TOP)
Button(top,text='아래쪽',width=10).pack(side=BOTTOM)
Button(top,text='왼쪽',width=10).pack(side=LEFT)
Button(top,text='오른쪽',width=10).pack(side=LEFT)


mainloop()
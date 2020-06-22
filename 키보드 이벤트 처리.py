from tkinter import *

top=Tk()

def key(event):
    print(event.char,"가 눌려졌습니다.")

def mouse(event):
    frm.focus_set()
    print("<마우스로 프레임의 포커스 설정함>")

frm=Frame(top,width=100,height=100)
frm.pack()

frm.bind("<Key>",key)
frm.bind("<Button-1>",mouse)

top.mainloop()
from tkinter import *

top=Tk()
top.title("이벤트 처리")

def mleft(event):
    print(event.x,event.y,'에서 마우스 클릭')

def mright(event):
    print('Right Button, 끝내기')
    import sys; sys.exit()

fr=Frame(top,width=240,height=100)
fr.bind("<Button-1>",mleft)
fr.bind("<Button-3>",mright)
fr.pack()

top.mainloop()
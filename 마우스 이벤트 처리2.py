from tkinter import *

def sleft(event):
    print("단일클릭, 왼쪽버튼")

def dleft(event):
    print("더블클릭, 왼쪽 버튼")

bt=Button(None, text="마우스 클릭")
bt.pack()

bt.bind('<Button-1>',sleft)
bt.bind('<Double-1>',dleft)

bt.mainloop()
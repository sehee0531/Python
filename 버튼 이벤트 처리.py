from tkinter import *

top=Tk()

def ft():
    lb1["text"]="클릭했습니다."

lb1=Label(top)
lb1.pack()

bt1=Button(top,text="클릭하세요!",command=ft)
bt1.pack()

top.mainloop()
from tkinter import *

top=Tk()

def calc(event):
    lb.configure(text="결과 : "+str(eval(ent.get())))

lb1=Label(top,text="파이썬 수식 입력 : ")
lb1.pack()

ent=Entry(top)
ent.bind("<Return>",calc)
ent.pack()

lb=Label(top,text="결과 : ")
lb.pack()

top.mainloop()
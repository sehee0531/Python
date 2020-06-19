from tkinter import *

top=Tk()
top.title("라디오 버튼")

ch=IntVar

def choice():
    s=ch.get()
    if s==1:
        img = PhotoImage(file="dog.gif")
    elif s==2:
        img = PhotoImage(file="cat.gif")
    elif s==3:
        img = PhotoImage(file="rabbit.gif")
    elif s==4:
        img = PhotoImage(file="bird.gif")
    lb2=Label(fr,image=img)
    lb2.image=img
    lb2.grid(row=0,colun=1,rowspan=10)

lb1=Label(top,text="가장 선호하는 동물을 고르시오 : ")
lb1.pack()

fr=Frame(top)
fr.pack(side=LEFT)

rb1=Radiobutton(top,text="개",variable=ch,value=1, command=choice)
rb1=Radiobutton(top,text="고양이",variable=ch,value=2, command=choice)
rb1=Radiobutton(top,text="토끼",variable=ch,value=3, command=choice)
rb1=Radiobutton(top,text="새",variable=ch,value=4, command=choice)
rb1.grid(row=0,column=0,sticky=W)
rb2.grid(row=1,column=0,sticky=W)
rb3.grid(row=2,column=0,sticky=W)
rb4.grid(row=3,column=0,sticky=W)

top.mainloop()
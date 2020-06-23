from tkinter import *

top=Tk()
top.title("스톱워치")

cnt=0
def StopWatch():
    if running:
        global cnt
        cnt+=1
        lb1.config(text=str(cnt))
    top.after(1000,StopWatch)

def Start():
    global running
    running=True

def Stop():
    global running
    running=False

def Reset():
    global cnt
    cnt=0
    lb1.config(text=str(cnt))

lb1=Label(top,fg="blue")
lb1.pack()

running=False
StopWatch()

bt1=Button(top,text="Start",padx=10,width=25,command=Start).pack()
bt2=Button(top,text="Stop",padx=10,width=25,command=Stop).pack()
bt3=Button(top,text="Reset",padx=10,width=25,command=Reset).pack()

top.mainloop()


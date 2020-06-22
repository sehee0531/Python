from tkinter import *

top=Tk()

def motion(event):
    print("Mouse position : (",event.x,event.y,")")

 
st='''마우스를 움직이면 마우스의 위치를 출력한다'''

msg=Message(top,text=st,bg="skyblue",font=("times",18))

msg.pack()

msg.bind("<Motion>",motion)

mainloop()
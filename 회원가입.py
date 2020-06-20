from tkinter import *

top=Tk()
userinfo={"username" : "sehee","password" : "1234"}

def login():
    if str(en1.get())==str(userinfo["username"])and str(en2.get())==str(userinfo["password"]):
        lb3["text"]="인증이 완료되었습니다."
    else:
        lb3["text"]="아이디 또는 비밀번호가 잘못 되었습니다."


lb1=Label(top,text='username')
lb2=Label(top,text='password')
lb3=Label(top)
en1=Entry(top)
en2=Entry(top)
bt1=Button(top,text='인증',command=login)

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
lb3.grid(row=2,column=1)
en1.grid(row=0,column=1)
en2.grid(row=1,column=1)
bt1.grid(row=0,column=2,rowspan=2)

top.mainloop()
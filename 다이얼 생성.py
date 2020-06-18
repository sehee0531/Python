from tkinter import *

top=Tk()

number=[['1','2','3'],
         ['4','5','6'],
         ['7','8','9'],
         ['*','0','#']]

for a in range(4):
    for b in range(3):
        bt1=Label(top,padx=10,relief=RAISED,text=number[a][b])
        bt1.grid(row=a,column=b)

top.mainloop()
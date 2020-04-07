name1=str(input("이름 첫째자는 :"))
name2=str(input("이름 둘째자는 :"))
name3=str(input("이름 셋째자는 :"))

a1=chr(ord(name3[0])+32)
a2=chr(ord(name2[0])+32)
a3=chr(ord(name1[0])+32)+name1[1:]

length=len(name1)+len(name2)+len(name3)
star="*"*length+"\n"

print(star,a2+a1+a3)

import turtle

t=turtle.Turtle()
t.shape("turtle")

t.goto(0,0)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)

t.up()
t.hideturtle()
t.goto(5,30)
t.color("red")
t.write("Stop",font=(25))


turtle.done()

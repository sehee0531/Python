import turtle

t=turtle.Turtle()
t.shape("turtle")


a=int(input("x1 :"))
b=int(input("y1 :"))
c=int(input("x2 :"))
d=int(input("y2 :"))
e=int(input("x3 :"))
f=int(input("y3 :"))

t.up()
t.goto(a,b)
t.down()
t.goto(c,d)

t.goto(e,f)

turtle.done()


import turtle

t=turtle.Turtle()
t.shape("turtle")


x1=float(input("x1 :"))
y1=float(input("y1 :"))
x2=float(input("x2 :"))
y2=float(input("y2 :"))

a=("두점사이의 거리 =",((x1-x2)**2+(y1-y2)**2)**0.5)

t.goto(x1,y1)
t.goto(x2,y2)

t.up()
t.write(a)


turtle.done()
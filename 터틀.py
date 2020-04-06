import turtle

t=turtle.Turtle()
t.shape("classic")

n = int(input("길이를 입력하세요 : "))

t.goto(0,0)
t.circle(n)
t.forward(n)
t.left(90)
t.forward(n*2)
t.left(90)
t.forward(n*2)
t.left(90)
t.forward(n*2)
t.left(90)
t.forward(n*2)


turtle.done()
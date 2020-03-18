import turtle

t=turtle.Turtle()
t.shape("turtle")

t.goto(0,0)
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.goto(40,0)
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.goto(80,0)
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()
t.goto(120,0)
t.fillcolor("green")
t.begin_fill()
t.circle(50)
t.end_fill()


turtle.done()
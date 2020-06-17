import turtle

t=turtle.Turtle()
t.shape("turtle")

def five():
    list = [[0,0,'blue'], [100, 0 ,'black'], [200, 0,'red' ], [50, -50,'yellow' ], [150, -50,'green']]

    for x,y,c in list:
        t.up()
        t.goto(x,y)
        t.down()
        t.pensize(8)
        t.color(c,c)
        t.circle(50)

five()
t.hideturtle()


    
    
t.done()



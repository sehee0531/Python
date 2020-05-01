import turtle

t=turtle.Turtle()
t.shape("turtle")


for i in range(1,6,1):
    t.right(72)
    for j in range(0,5,1):

        t.forward(50)
        t.left(72)




   
t.hideturtle()
 
turtle.done()


for i in range(1,6):
    for j in range(0,1):
        print(" "*(5-i),"*"*(2*i-1))

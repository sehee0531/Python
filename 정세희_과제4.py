a=int(input("국어 점수는 :"))
b=int(input("수학 점수는 :"))
c=int(input("영어 점수는 :"))
d=int(input("과학 점수는 :"))
e=int(input("사회 점수는 :"))
sum=int(a+b+c+d+e)/5

list=[a,b,c,d,e]
print("입력자료: ",list)
list.sort()
list.reverse()
print("정렬자료: ",list)
print("평균점수: ", sum)


import turtle

t = turtle.Turtle()
t.shape("turtle")

list = ['red','green','blue']

t.goto(0,0)
t.fillcolor(list[0])
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()
t.goto(100,0)
t.fillcolor(list[1])
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()
t.goto(200,0)
t.fillcolor(list[2])
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()
t.hideturtle()


turtle.done()
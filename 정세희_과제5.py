import turtle

t = turtle.Turtle()
t.shape("classic")

a = int(turtle.textinput("Python Turtle Graph...","변1:"))
b = int(turtle.textinput("Python Turtle Graph...","변2:"))
c = int(turtle.textinput("Python Turtle Graph...","변3:"))

if a**2 + b**2 == c**2 :
    t.goto(0,0)
    t.forward(a*10)
    t.left(90)
    t.forward(b*10)
    t.goto(0,0)
    t.right()
    
else :
    t.goto(0,0)
    t.write("직각삼각형이 아님")
 

turtle.done()


a=int(input("a 입력 :"))
b=int(input("b 입력 :"))

if a>b:
    print("a가 b 보다",a-b," 만큼 더 크다")
elif b>a:
    print("b가 a 보다",b-a," 만큼 더 크다")
else:
    print("a 와 b는 같다")

import random

x = input("가위,바위,보 중 하나를 선택하시오 : ")
y = random.choice(['가위','바위','보'])

if y=="가위":
    print("컴퓨터가 낸 수 : 가위")
elif y=="바위":
    print("컴퓨터가 낸 수 : 바위")
elif y=='보':
    print("컴퓨터가 낸 수 : 보")

if x=='가위':
    x=0
elif x=='바위':
    x=1
elif x=='보':
    x=2

if x==y:
    print("무승부입니다")
elif x==0 and y=="바위":
    print("컴퓨터 승, user 패")
elif x==0 and y=='보':
    print("컴퓨터 패, user 승")
elif x==1 and y=="가위":
    print("컴퓨터 패, user 승")
elif x==1 and y=='보':
    print("컴퓨터 승, user 패")
elif x==2 and y=="가위":
    print("컴퓨터 승, user 패")
elif x==2 and y=="바위":
    print("컴퓨터 패, user 승")


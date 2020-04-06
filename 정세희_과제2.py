a=int(input("세자리 정수 입력"))
b=a//100
c=a%100
d=c//10
e=c%10
f=e//1
print("입력한 수의 역순",f,d,b)







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

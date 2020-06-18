import turtle
t=turtle.Turtle()

t.shape("turtle")

def cCircle(length):
    r=-a
    t.up()
    t.goto(0,r)
    t.down()
    t.circle(length)

             
a=0
leng=50
for n in range(3):
    cCircle(leng)
    leng=leng+30
    a=a+25
    t.up()
    t.goto(0,50)
    t.down()

def num1():
    b=[]
    a=int(input("10진수: "))


    while a!=0:
        b.append(a%2)
        a=a//2

    for i in range(len(b)-1,-1,-1):
        print(b[i],end=" ")

def num2():
    a=str(input("2진수:"))
    num=0
    b=len(a)-1

    for i in range(0,len(a),1):

        if a[i]=='0':

            num=num+0

        elif a[i]=='1':
            num=num+2**b
        b=b-1

    print(num)
        

print (num1())
print(num2())                                   
        


class Emp:
    pass

x=Emp()
y=Emp()

x.name='James'
x.age=37
print('Name',x.name,'age',x.age)
print('x.__dict__ :',x.__dict__)
print('y.__dict__ :',y.__dict__)
def plus(a,b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None

print(plus(12,12))
print(plus(12,"12")) 
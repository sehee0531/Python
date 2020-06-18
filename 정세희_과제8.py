s = input("문자열 입력 : ")

def p():
   print("회  |","*"*value)

d = dict()
for c in s:
   if c not in d:
       d[c]=1
   else:
       d[c] = d[c]+1


for key, value in d.items():
   print(key, ":", value,end=' ')
   p()
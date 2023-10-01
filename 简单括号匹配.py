from Stack import Stack
a=input()
s=Stack()
flag=True
for i in a:
    if i=='(':
        s.push(i)
    else:
        if not s.isEmpty():
            s.pop()
        else:
            flag=False
            break
if flag==False:
    print('incorrespondence')
elif not s.isEmpty():
    print('incorrespondence')
else :
    print('correspondence')
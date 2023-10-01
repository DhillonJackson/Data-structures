from Stack import Stack
s=Stack()
prec={}
prec['*']=3
prec['/']=3
prec['+']=2
prec['-']=2
prec['(']=1

expressionlst=input()
outputlst=[]
for i in expressionlst:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in  '0123456789':
        outputlst.append(i)
    elif i=='(':
        s.push(i)
    elif i==')':
        while s.peek()!='(':
            outputlst.append(s.pop())
    else:
        while not s.isEmpty() and prec[s.peek()]>=prec[i]:
            outputlst.append(s.pop())
        s.push(i)
while not s.isEmpty():
    if s.peek()!='(':
        outputlst.append(s.pop())
    else:
        s.pop()
print(''.join(outputlst))
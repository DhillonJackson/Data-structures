from Stack import Stack
a=input()
s=Stack()
flag=True
for i in a:
    if i in'({[':
        s.push(i)
    else:
        if not s.isEmpty() :
            if i==')' and s.peek()=='(':
                s.pop()
            elif i=='}' and s.peek()=='{':
                s.pop()
            elif i==']' and s.peek()=='[':
                s.pop()
            else:
                flag=False
                break
        else:
            flag=False
            break
if flag==False:
    print('incorrespondence')
elif not s.isEmpty():
    print('incorrespondence')
else :
    print('correspondence')
'''
一个小技巧：
def matches(open,close):
opens="([{"
closers=")]}"
return opens.index(open)==closers.index(close)   #避免使用多个if-else语句
'''
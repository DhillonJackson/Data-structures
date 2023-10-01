from Stack import Stack
s=Stack()
n=int(input())
#除k取余法
while n!=0:
    s.push(n%2)
    n=n//2
s.items.reverse()
strlist=[]
for i in s.items:
    strlist.append(str(i))
resstr=''.join(strlist)
print(resstr)
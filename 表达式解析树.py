#很成功
from Stack import Stack
from BinaryTree import BinaryTree
etree=BinaryTree('')
s=Stack()
expression='(3+(4*5))'
lst=list(expression)
current=etree
s.push(current)
for i in lst:
    if i=='(':
        
        current.insertleft('')
        s.push(current)
        current=current.left
    elif i in '+-*/':
        
        current.setroot(i)
        current.insertright('')
        s.push(current)
        current=current.right
    elif i in '0123456789':
        current.setroot(i)
        current=s.pop()
    else:
        current=s.pop()
present=etree
print(present.left.root)
#很成功
from Stack import Stack
from BinaryTree import BinaryTree
import operator
'''etree=BinaryTree('')
s=Stack()
expression='3+(4*5)'
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
'''
etree=BinaryTree('')
etree.root='*'
etree.left=BinaryTree(6)
etree.right=BinaryTree(4)

def evaluate(tree):
    operation={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    left=tree.left
    right=tree.right
    #   注意fn=operation[tree.root]一定不能写在这里  一定要写在if的判断语句里面  如果这个树只有根节点 字典会报错keyerror
    if left and right:
        fn=operation[tree.root]
        return fn(evaluate(left),evaluate(right))
    else:
        return tree.root

print(evaluate(etree))

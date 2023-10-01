def count(tree):
    if tree:
        return 1+count(tree.left)+count(tree.right)
    else:
        return 0
    

            #以下是一个有四个节点的BinaryTree

#递归啊家人们
from BinaryTree import BinaryTree
tree=BinaryTree('*')
tree.insertleft('3')
tree.insertright('6')
current=tree.GetLeftTree()
current.insertleft('3左下')
#先根节点  再左树   再右树
def travel1(tree):
    if tree:
        print(tree.root)
        travel1(tree.left)
        travel1(tree.right)

#先左树  再根节点   再右树
def travel2(tree):
    if tree:
       
        travel2(tree.left)
        print(tree.root)
        travel2(tree.right)

#先左树  再右树  再根节点
def travel3(tree):
    if tree:
        
        travel3(tree.left)
        travel3(tree.right)
        print(tree.root)

'''travel1(tree)
print('----------------------')
travel2(tree)
print('----------------------')
travel3(tree)
print('----------------------')'''

print(count(tree))  #成功输出4
class BinaryTree():
    def __init__(self,root) -> None:
        self.root=root
        self.left=None
        self.right=None
    def GetLeftTree(self):
        return self.left
    def GetRightTree(self):
        return self.right
    def insertleft(self,new):
        temp=BinaryTree(new)
        if self.left==None:
            self.left=temp
        else:
            temp.left=self.left
            self.left=temp
    def insertright(self,new):
        temp=BinaryTree(new)
        if self.right==None:
            self.right=temp
        else:
            temp.right=self.right
            self.right=temp
    def setroot(self,name):
        self.root=name
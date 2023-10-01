class Node():
    def __init__(self,name):
        self.data=name
        self.next=None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,newname):
        self.data=newname
    def setnext(self,newnext):
        self.next=newnext

class UnorderedList():
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp
    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.next
        return count
    def search(self,target):
        current=self.head
        found=False
        while current !=None and not found:
            if current.data==target:
                found=True
                return found
            else:
                current=current.next

                

lianbiao=UnorderedList()
lianbiao.add('lisi')
lianbiao.add('wamgwu')
lianbiao.add('wangermazi')
lianbiao.add('sb')
print(lianbiao.size())
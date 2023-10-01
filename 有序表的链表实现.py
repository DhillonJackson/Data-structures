import random
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

class OrderedList():
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        current=self.head
        #注意一个点  就是保持self.head 如果加入到表头，则self.head指向表头，否则指向不变
        if self.head==None:
            self.head=temp
            temp.next=None
        elif self.head.data>=temp.data:
            temp.next=self.head
            self.head=temp
        else:
            while current!=None and current.next!=None:
                if current.data<=temp.data<=current.next.data:
                    temp.next=current.next
                    current.next=temp
                    break   #这个break太重要了  如果不写就一直死循环
                else:
                    current=current.next
            if current.next==None:
                current.next=temp
                temp.next=None
lst=OrderedList()
for i in [0,-12,999,45,32]:
    lst.add(i)

while lst.head!=None:
    print(lst.head.data)
    lst.head=lst.head.next

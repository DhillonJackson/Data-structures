class Queue():
    def __init__(self) -> None:
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()  #一定要return
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    
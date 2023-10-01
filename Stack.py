class Stack():
    def __init__(self) -> None:
        self.items=[]
    def peek(self):
        return(self.items[-1])
    def push(self,a):
        self.items.append(a)
    def pop(self):
        return self.items.pop()
    def size(self):
        return(len(self.items))
    def isEmpty(self):
        return not bool(self.items)
    def showstack(self):
        print(self.items)
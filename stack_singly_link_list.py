class node:
    def __init__(self,itm = None, next = None):
        self.itm = itm
        self.next = next

class stack :
    def __init__(self) -> None:
        self.start = None
        self.kount = 0

    def is_empty(self):
        return self.start == None
    
    def push(self,data):
        n = node(data,self.start)
        self.start = n
        self.kount +=1
    
    def pop(self):
        if not self.is_empty():
            data = self.start.itm
            self.start = self.start.next
            self.kount-=1
            return data
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.itm
        else:
            raise self.is_empty()
        
    def size(self):
        return self.kount

mylist = stack()
mylist.push(10)
mylist.push(20)
mylist.push(30)
print(mylist.size())
print(mylist.peek())
mylist.pop()
print(mylist.size())
print(mylist.peek())

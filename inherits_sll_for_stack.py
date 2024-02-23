from singly_link_list import *

class stack(sll):
    def __init__(self):
        # it help to kall the init method of parent class which is sll 
        super().__init__()
        self.kount = 0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.kount +=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.kount -=1
        
    def peek(self):
        if not self.is_empty():
            return self.start.itm
        
    def size(self):
        return self.kount
s = stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
print(s.peek())
s.pop()
print(s.size())
print(s.peek())
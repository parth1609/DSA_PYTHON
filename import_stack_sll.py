from singly_link_list import *

class stack:
    def __init__(self):
        # create the obj of singly link list which is imported
        self.mylist = sll()
        self.kount = 0
    def is_empty(self):
        # import is_empty() function from the singly_link_list
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.kount+=1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.kount-=1
        
        
    def peek(self):
         if not self.is_empty():
             return self.mylist.start.itm
    
    def size(self):
            return self.kount
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.size())
print(s.peek())
s.pop()
print(s.size())
print(s.peek())

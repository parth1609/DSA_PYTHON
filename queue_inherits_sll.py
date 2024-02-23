from singly_link_list import *

class qu(sll):
    def __init__(self, start=None):
        super().__init__(start)
        self.kount =0
    def is_empty(self):
        return super().is_empty()
    def enqueue(self,data):
        self.insert_at_last(data)
        self.kount+=1
    def dequeue(self):
        if not self.is_empty():
            self.delete_first()
            self.kount -=1

    def get_front(self):
        if not self.is_empty():
            return self.start.itm
    
    def get_rear(self):
        tmp = self.start
        if not self.is_empty():
            while tmp.next is not None:
                tmp = tmp.next
            print(tmp.itm)
        
    
    def size(self):
        return self.kount
    
    def printlist(self):
        tmp = self.start
        if not self.is_empty():
            while tmp is not None:
                print(tmp.itm,end=' ')
                tmp = tmp.next
            

s= qu()
s.enqueue(10)  
s.enqueue(20)  
s.enqueue(30) 
s.enqueue(40)
s.printlist() 

print(" ")
s.dequeue()
print(s.get_front())
print(s.get_rear())
s.printlist() 
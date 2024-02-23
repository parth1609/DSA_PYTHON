from singly_link_list import *

class qu:
    def __init__(self) -> None:
        self.mylist = sll()
        self.kount =0
    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self,data):
        self.mylist.insert_at_last(data)
        self.kount +=1
    
    def dequeue(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.kount -=1
    
    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.itm
    
    def get_rear(self):
        tmp = self.mylist.start
        if not self.is_empty():
            while tmp is None:
                print(tmp.mylist.itm)
                tmp = tmp.next

    def size(self):
        return self.kount
    
    def printlist(self):
        for i in self.mylist:
            print(i,end=" ")


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
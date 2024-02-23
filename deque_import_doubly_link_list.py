from doubly_link_list import *

class dequ:
    def __init__(self) :
          self.mylist = dll()
          self.rear = None
          self.kount = 0
    
    def is_empty(self):
        return self.mylist.is_empty()
    
    def insert_front(self,data):
        self.mylist.insert_at_start(data)
        self.kount +=1
    
    def insert_rear(self,data):
        self.mylist.insert_at_last(data)
        self.kount +=1
        
    def delete_front(self):
        if not self.is_empty():
            self.mylist.delete_first()
        else:
            raise IndexError("mpty list ")
        self.kount -=1
        
    def delete_rear(self):
        if not self.is_empty():
            self.mylist.delete_last()
        else:
            raise IndexError("mpty list ")
        self.kount -=1

    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.itm
        else:
            raise IndexError("mpty list ")

    def get_rear(self):
        if not self.is_empty():
            tmp = self.mylist.start
            while tmp is None:
                print(tmp.mylist.itm)
                tmp = tmp.next
        else:
            raise IndexError("mpty list ")
        
    def size(self):
        return self.kount
    
    

k = dequ()

    
k.insert_front(10)
k.insert_front(20)
k.insert_front(50)
k.insert_rear(30)
k.insert_rear(40)
print(k.size())

k.delete_front()
k.delete_rear()

print(k.size())
try:
    print("front is ",k.get_front(),"Rear is ",k.get_rear())
except IndexError as a:
    print(a.args[0])

class node:
    def __init__(self,itm = None,prv= None, next = None):
        self.itm = itm
        self.prv = prv
        self.next = next
     

class dequ:
    def __init__(self):
        self.front = None
        self.rear = None
        self.kount = 0
    
    def is_empty(self):
        return self.front == None
    
    def insert_front(self,data):
        n = node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prv = n
        self.front = n
        self.kount +=1

    def insert_rear(self,data):
        n = node(data,self.rear,None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.kount+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("mpty list")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prv = None
        self.kount -=1
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("mpty list")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prv
            self.rear.next = None
        self.kount-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("mpty list")
        return self.front.itm

    def get_rear(self):
        if self.is_empty():
            raise IndexError("mpty list")
        return self.rear.itm

    def size(self):
        return self.kount
    
    def printlist(self):
        tmp = self.front
        while tmp == self.rear:
            print(tmp.itm, end=' ')
        tmp = tmp.next
    



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

k.printlist()
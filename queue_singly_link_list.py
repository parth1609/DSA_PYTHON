class node:
    def __init__(self,itm = None,next = None):
        self.itm  = itm
        self.next = next
class qu:
    def __init__(self,start = None):
        self.start = start
        self.kount = 0
    def is_empty(self):
        return self.start == None
    
    def enqueue(self,data):
        n = node(data)
        if not self.is_empty():
            tmp = self.start
            while tmp.next is not None:
                tmp= tmp.next
            tmp.next = n
        else:
            self.start = n
        self.kount+=1
    def dequeue(self):
        if not self.is_empty():
            self.start = self.start.next
            self.kount-=1
        return None
    
    def get_front(self):
        if not self.is_empty():
            return self.start.itm
        return None
    
    def get_rear(self):
        if not self.is_empty():
            tmp = self.start
            while tmp.next is not None:
                tmp = tmp.next
            print(tmp.itm)
        else:
            return None
            
    def size(self):
        return self.kount
    
    def printlist(self):
        tmp = self.start
        while tmp is not None:
            print(tmp.itm,end=' ')
            tmp = tmp.next

s= qu()
s.enqueue(10)  
s.enqueue(20)  
s.enqueue(30) 
s.enqueue(40)
print(s.size())
s.printlist()
print(" ")
s.dequeue()
print(s.size())
print(s.get_front())
print(s.get_rear())
s.printlist()

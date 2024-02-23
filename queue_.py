# queue by using creating a list & prform the opration
class qu:
    def __init__(self) -> None:
        self.mylist = []

    def is_empty(self):
        return len(self.mylist) == 0
    
    def enqueue(self,data):
        self.mylist.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("quu is underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("quu is underflow")
        
    def size(self):
        return len(self.mylist   )
    
    def printlist(self):
        for i in self.mylist:
            print(i,end=" ")


s= qu()
try:
    print(s.get_front())
except IndexError as e:
    print(e.args[0])

s.enqueue(10)  
s.enqueue(20)  
s.enqueue(30) 
s.enqueue(40)

print("front = ", s.get_front(),"rear = ",s.get_rear())
try:
    s.dequeue()
    print("siz is ", s.size())
except IndexError as e:
    print(e.args[0])

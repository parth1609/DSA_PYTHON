class dequ(list):
    def is_empty(self):
        return len(self) == 0
    
    def insert_front(self,data):
        self.insert(0,data)
    
    def insert_rear(self,data):
        self.append(data)

    def delete_front(self):
        if not self.is_empty():
            return super().pop(0)
        else:
            raise IndexError("empty list")
        
    def delete_rear(self):
        if not self.is_empty():
            return super().pop(-1)
        else:
            raise IndexError("empty list")
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("empty list")
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("empty list")
        
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("empty list")
        
    def printlist(self):
        for i in self:
            print(i,end=' ')


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
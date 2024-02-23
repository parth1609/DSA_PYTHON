class dequ:
    def __init__(self) -> None:
        self.mylist = []
        self.kount = 0
    
    def is_empty(self):
        return len(self.mylist) == 0
    
    def insert_front(self,data):
        if  not self.is_empty():
            self.mylist.insert(0,data)
            
        else:
            self.mylist.append(data)
        self.kount +=1
    
    def insert_rear(self,data):
        if not self.is_empty():
            self.mylist.append(data)
            self.kount +=1
    
    def delete_front(self):
        if not self.is_empty():
            self.mylist.pop(0)
            self.kount -=1
        else:
            raise IndexError("empty  list ")
    
    def delete_rear(self):
        if not self.is_empty():
            self.mylist.pop(-1)
            self.kount -=1
        else:
            raise IndexError("empty  list ")

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("empty  list ")
        
    def get_rear(self):
        if not self.is_empty():
                return self.mylist[-1]
        else:
                raise IndexError("empty  list ")
        

    def size(self):
        return self.kount

    def printlist(self):
        for i in self.mylist:
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
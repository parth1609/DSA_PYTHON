class PriorityQu:
    def __init__(self) -> None:
        self.mylist = []
    
    def push(self,data,priority):
        index = 0
        while index<len(self.mylist) and self.mylist[index][1]<=priority:
            index+=1
        self.mylist.insert(index,(data, priority))

    def is_empty(self):
        return len(self.mylist)==0
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Th priority qu is null ")
        return self.mylist.pop(0)[0]
    
    def size(self):
        return len(self.mylist)
    

p = PriorityQu()
p.push("amit",1)
p.push("parth",2)
p.push("amita",8)
p.push("atul",5)
p.push("ashish",4)
while not p.is_empty() :
    print(p.pop())
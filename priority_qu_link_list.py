class node:
    def __init__(self,itm = None, prioriy = None, next = None):
        self.itm = itm
        self.prioriy = prioriy
        self.next = next

class PriorityQu:
    def __init__(self) -> None:
        self.start = None
        self.kount = 0
    
    def push(self,data,prioriy):
        n= node(data,prioriy)
        if not self.start or prioriy < self.start.prioriy:
            n.next = self.start
            self.start = n
        else:
            tmp = self.start
            while tmp.next and tmp.next.prioriy<= prioriy:
                tmp = tmp.next
            n.next = tmp.next
            tmp.next = n
        self.kount+=1

    def is_empty(self):
        return self.start == None
    
    def pop(self):
        if self.is_empty():
            raise IndexError("null")
        data = self.start.itm
        self.start = self.start.next
        self.kount-=1
        return data
    
    def size(self):
        return self.kount


p = PriorityQu()
p.push("amit",1)
p.push("parth",2)
p.push("amita",8)
p.push("atul",5)
p.push("ashish",4)
while not p.is_empty() :
    print(p.pop())
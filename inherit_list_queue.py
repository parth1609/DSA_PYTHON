
class qu(list):
    def __init__(self):
        self.kount = 0
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self,data):
        self.append(data)
        self.kount +=1

    
    def dequeue(self):
        if  not self.is_empty():
            self.kount-=1
            return super().pop(0)
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]

    def size(self):
        return self.kount
s = qu()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.enqueue(40)
print(s.size())
print(s.dequeue())
print(s.size())
print(s.get_front())
print(s.get_rear())
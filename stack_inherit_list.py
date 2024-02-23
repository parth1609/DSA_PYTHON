class stack(list):# here list is inherited as self
    
    def is_empty(self):
        return len(self) == 0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stak is mpty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stak is mpty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("no atrributr 'insrt' ")
    def printlist(self):
        print(self)

s1 = stack()
# s1.insert(0,10)
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
s1.printlist()

''' stack using list'''


class stack :
    def __init__(self) -> None:
        self.itm = []
    def is_empty(self):
        return len(self.itm) == 0
    # append the itm in the stack at the top
    def push(self,data):
        self.itm.append(data)
    # delete the top most itm in the stack
    def pop(self):
        if not self.is_empty():
            return self.itm.pop()
        else:
            raise  IndexError(" stack is empty")
    # return the top most itm in the stack
    def peek(self):
        if not self.is_empty():
            return self.itm[-1]
        else:
            raise  IndexError(" stack is empty")
    def size(self):
        return len(self.itm)
    
s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.pop())
print(s1.peek())

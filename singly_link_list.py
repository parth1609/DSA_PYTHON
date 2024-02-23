'''singly link list'''
# surabhsukla.com

# define a class node to dsescribe of singly link list
class node:
    def __init__(self,itm= None, next=None):
        self.itm = itm
        self.next = next

# define a class sll to Implement singly link list with __init__ function to initialis th singly link list
class sll:
    def __init__(self, start=None):
        self.start = start

# define  a function to check if th sll is_empty
    def is_empty(self):
        return self.start == None
    
# define  a function to insrt the itm at start of sll
    def insert_at_start(self,data):
        n = node(data,self.start)
        self.start = n  

# define  a function to insrt the itm at last of sll
    def insert_at_last(self,data):
        n = node(data)
        if not self.is_empty():
            temp  = self.start
            while temp.next is not None:
                temp  = temp.next
            temp.next = n
        else:
            self.start = n

# search th itm data at particular node & return the node
    def search(self,data):
        temp  = self.start
        while temp  is not None:
            if temp.itm == data:
                return temp 
            temp  = temp.next
        return None
    
# define any particular node after nth node
    def insert_after(self,temp,data):
        if temp  is not None:
            n = node(data,temp.next)
            temp.next = n

# print all itm in list
    def printlist(self):
        temp  = self.start
        while temp  is not None:
            print(temp.itm,end=' ')
            temp = temp.next

# delete the first itm in the list
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

# delete the last itm in the list
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp= self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

# delete the last itm in the list
    def delete_itm(self,data):
        if self.start is None:
            pass
        elif self.start.next is None :
            if self.start.itm == data:
                self.start = None
        else:
            temp = self.start
            if temp.itm == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.itm == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    
    def __iter__(self):
        return sllitrator(self.start)

#iteate th singly link list using for loop
class sllitrator:
    def __init__(self,start):
        self.kurr = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.kurr:
            raise StopIteration
        data = self.kurr.itm
        self.kurr = self.kurr.next
        return data
        




                
# Test program
'''
mylist = sll()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)  
mylist.printlist()
mylist.search(20)
print("")
# mylist.delete_itm(10)
mylist.printlist()
print(" ")
for x in mylist:
    print(x)
'''









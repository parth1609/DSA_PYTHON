'''circular_link_list'''

class node:
    def __init__(self, itm = None, next = None):
        self.itm = itm
        self.next = next
class cll:
    def __init__(self,last = None):
        self.last = last
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        n = node(data)
        if  self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
        
    def insert_at_last(self,data):
        n = node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
        
    def search(self,data):
        if self.is_empty():
            return None
        tmp = self.last.next
        while tmp != self.last:
            if tmp.itm == data:
                return tmp
            tmp = tmp.next
        if tmp.itm == data:
            return tmp
        return None
    
    def insert_after(self,tmp, data):
        if tmp is not None:
            n = node(data, tmp.next)
            tmp.next = n
            if tmp==self.last:
                self.last = n

            
    
    def printlist(self):
        if not self.is_empty(): 
            tmp = self.last.next
            while tmp != self.last:
                print(tmp.itm, end=' ')
                tmp = tmp.next
            print(tmp.itm)

    def delete_first(self):
        if self.last == None:
            pass
        elif self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def delete_last(self):
        if self.last == None:
            pass
        elif self.last.next == self.last:
            self.last = None
        else:
            tmp = self.last.next
            while tmp.next!= self.last:
                tmp = tmp.next
            tmp.next = self.last.next
            self.last = tmp

    def delete_itm(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.itm == data:
                    self.last = None
            else:
                if self.last.next.itm == data:
                     self.delete_first()
                tmp = self.last.next
                while tmp.next != self.last:
                    if tmp.next.itm == data:
                        tmp.next = tmp.next.next
                    tmp = tmp.next
                if tmp.next == self.last:
                    if tmp.next.itm == data:
                        tmp.next = self.last.next
                        self.last = tmp
                
    def __iter__(self):
        if self.last == None:
            return cllitrator(None)
        else:
            return cllitrator(self.last.next)
class cllitrator:
    def __init__(self,start) :
        self.kurr = start
        self.start  = start
        self.kount = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.kurr == None:
            raise StopIteration
        if self.kurr == self.start and self.kount ==1:
            raise StopIteration
        else:
            self.kount = 1
        data = self.kurr.itm
        self.kurr = self.kurr.next
        
        return data




mylist =  cll()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_after(mylist.search(30),25)
mylist.printlist()
mylist.delete_itm(30)
mylist.printlist()
print(" ")
for i in mylist:
    print(i,end=' ')
        
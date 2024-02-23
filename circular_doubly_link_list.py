class node:
    def __init__(self, itm = None,next = None,prv = None) :
        self.prv = prv
        self.itm = itm
        self.next = next
class cdll:
    def __init__(self,start = None):
        self.start = start
    def is_empty(self):
        return self.start == None 
    def insert_at_start(self,data):
        n = node(data)
        if self.is_empty():
            n.next = n
            n.prv = n
        else:
            n.next = self.start
            n.prv = self.start.prv
            self.start.prv.next = n
            self.start.prv = n
        self.start = n
    def insert_at_last(self,data):
        n = node(data)
        if self.is_empty():
            n.next = n
            n.prv = n
            self.start = n
        else:
            n.next = self.start
            n.prv = self.start.prv
            n.prv.next = n
            self.start.prv = n
    def search(self,data):
        tmp = self.start
        if tmp == None:
            return None
        if tmp.itm == data:
            return tmp
        else:
            tmp = tmp.next

        while tmp != self.start:
            if tmp.itm == data:
                return tmp
            tmp = tmp.next
        return None
    def insert_after(self,tmp,data):
        if tmp is not None:
            n = node(data)
            n.next = tmp.next
            n.prv = tmp
            tmp.next.prv = n
            tmp.next = n
    def printlist(self):
        tmp = self.start
        if tmp is not None:
            print(tmp.itm,end=' ')
            tmp = tmp.next
            while tmp != self.start:
                print(tmp.itm,end=' '  )
                tmp = tmp.next

    def delete_first(self):
        if not self.is_empty():
            if self.start.prv== self.start:
                self.start = None
            else:
                self.start.prv.next = self.start.next
                self.start.next.prv = self.start.prv
                self.start = self.start.next

    def delete_last(self):
        if not self.is_empty():
            if self.start.next== self.start:
                self.start = None
            else:
                self.start.prv.prv.next = self.start
                self.start.prv = self.start.prv.prv
        
         
    def delete_itm(self,data):
        if not self.is_empty():
            tmp = self.start
            if tmp.itm == data:
                self.delete_first()
            else:
                tmp = tmp.next
                while tmp != self.start:
                    if tmp.itm == data:
                        tmp.next.prv = tmp.prv
                        tmp.prv.next = tmp.next
                    tmp = tmp.next
    
    def __iter__(self):
        return cdllitrator(self.start)
    
class cdllitrator:
    def __init__(self,start) :
        self.kurr = start
        self.start = start
        self.kount = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.kurr is None:
            raise StopIteration
        if self.kurr == self.start and self.kount ==1:
            raise StopIteration
        else:
            self.kount = 1
        
        data = self.kurr.itm
        self.kurr = self.kurr.next

        return data

mylist = cdll()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(10),5)
mylist.printlist()
print("")
mylist.delete_itm(30)

mylist.printlist()
print(" ")
for x in mylist:
    print(x,end=' ')
            
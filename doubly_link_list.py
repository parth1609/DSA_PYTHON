class node:
    def __init__(self,prv= None, itm = None, next = None):
        self.prv = prv
        self.itm = itm
        self.next = next

class dll:
    def __init__(self,start= None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = node(None,data,self.start)
        if not self.is_empty():
            self.start.prv = n
        self.start = n

    def insert_at_last(self,data):
        tmp = self.start
        if self.start != None:
            while tmp.next != None:
                tmp = tmp.next 
        
        n = node(tmp, data)
        if tmp == None:
            self.start = n
        else:
            tmp.next  = n           

    def search(self,data):
        tmp = self.start
        while tmp is not None:
            if tmp.itm == data:
                return tmp
            tmp = tmp.next
        return None
    
    def insert_after(self,tmp,data):
        if tmp is not None:
            n = node(tmp,data,tmp.next)
            if tmp.next is not None:
                tmp.next.prv = n
            tmp.next = n
             

    
    def printlist(self):
        tmp = self.start
        while tmp is not None:
            print(tmp.itm, end=' ')
            tmp = tmp.next

    def delete_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prv = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            tmp = self.start
            while tmp.next is not None:
                tmp = tmp.next
            tmp.prv.next = None
    
    def delete_itm(self,data):
        if self.start is None:
            pass
         
        else:
            tmp = self.start
            while tmp is not None:
                if tmp.itm == data:
                    if tmp.next is not None:
                        tmp.next.prv = tmp.prv
                        # why elif is giving a error in next below line
                    if tmp.prv is not None:
                        tmp.prv.next = tmp.next
                    else:
                        self.start = tmp.next
                    break
                tmp = tmp.next
        
    def __iter__(self):
        return dllitrator(self.start)

class dllitrator:
    def __init__(self,start) :
        self.kurr = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.kurr:
            raise StopIteration
        data = self.kurr.itm
        self.kurr = self.kurr.next
        return data

'''
mylist = dll()
mylist.insert_at_start(20)
mylist.insert_at_start(40)
mylist.insert_at_last(200)
mylist.insert_after(mylist.search(20),25)

print(" ")
mylist.delete_itm(20)
for i in mylist:
    print(i,end=' ')
'''
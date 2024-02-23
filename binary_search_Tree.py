class node:
    def __init__(self,itm= None,left = None,right = None):
        self.itm = itm
        self.left = left
        self.right = right

class BST:
    def __init__(self,root = None):
        self.root = root
        self.kount = 0

    def insert(self, data):
        self.root = self.rinsert(self.root,data)
        
    
    def rinsert(self,root,data):
        if root is None:
            return node(data)
        if data < root.itm:
            root.left = self.rinsert(root.left,data)
        elif data > root.itm:
            root.right = self.rinsert(root.right,data)
        return root


    def search(self,data):
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if root is None or root.itm == data:
            return root
        if data < root.itm:
            return self.rsearch(root.left,data)
        elif data >root.itm:
            return self.rsearch(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result) 
            result.append(root.itm)
            self.rinorder(root.right,result)

    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:
            result.append(root.itm)
            self.rpreorder(root.left,result) 
            self.rpreorder(root.right,result)

    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result) 
            self.rpostorder(root.right,result)
            result.append(root.itm)

    def min_val(self,tmp):
        current = tmp
        while current.left is not None:
            current = current.left
        return current.itm
    
    def max_val(self,tmp):
        current = tmp
        while current.right is not None:
            current = current.right
        return current.itm
    
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
        

    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.itm:
            root.left = self.rdelete(root.left,data)
        elif data > root.itm:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.itm = self.min_val(root.right)
            self.rdelete(root.right,root.itm)
        return root
    
    def size(self):
        return len(self.inorder())

s = BST()
s.insert(50)
s.insert(40)
s.insert(10)
s.insert(65)
s.insert(60)
s.insert(80)



    
   
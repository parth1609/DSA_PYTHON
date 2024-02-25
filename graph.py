class graph:
    def __init__(self,vno):
        self.vertex_kount = vno
        self.adj_matrix = [ [0] * vno for i in range(vno)]

    def add_edge(self,u,v,weight =1):
        if 0<=u<self.vertex_kount and 0<=v<self.vertex_kount:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("invalid vertex")
    
    def remov_edge(self,u,v):
        if 0<=u<self.vertex_kount and 0<=v<self.vertex_kount:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("invalid vertex")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_kount and 0<=v<self.vertex_kount:
            return self.adj_matrix[u][v] != 0
        else:
            print("invalid vertex")
     
    def print_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))

a = graph(5)
a.add_edge(0,1)
a.add_edge(1,2)
a.add_edge(1,3)
a.add_edge(2,3)
a.add_edge(3,4)
a.print_matrix()
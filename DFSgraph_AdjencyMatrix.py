class grapph:

    def __init__(self,vertices):
        self.vertices=vertices
        self.adjency_matrix=[[0 for _ in range(self.vertices)] for _ in range(self.vertices)]

    def addEdge(self,u,v):
        if 0<=u<self.vertices and 0<=v<self.vertices:
            self.adjency_matrix[u][v]=self.adjency_matrix[v][u]=1
            return
        print(" Invalid Edge Inserted Try Again...")
    
    def display(self):
        print("Adjecency Matrix:")
        for row in self.adjency_matrix:
            print(row)
    
    def dfs_util(self,start,visited,dfs_order):
        visited[start]=True
        dfs_order.append(start)
        for i in range(self.vertices):
            if self.adjency_matrix[start][i]==1 and not visited[i]:
                self.dfs_util(i,visited,dfs_order)

    #dfs start here
    def dfs_traversal(self,start):
        visited=[False]*self.vertices
        dfs_order=[]
        self.dfs_util(start,visited,dfs_order)
        return dfs_order 
    

vertices=int(input("Enter The Total Number Of Vertices :"))
g=grapph(vertices)

while True:
    print()
    print("1. Add Route (Edge)")
    print("2. Display Adjacency Matrix")
    print("3. Perform DFS Traversal")
    print("4. Exit")
    print()
    
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        u = int(input("Enter starting location (node number): "))
        v = int(input("Enter connected location (node number): "))
        g.addEdge(u, v)

    elif choice == 2:
        g.display()

    elif choice == 3:
        start = int(input("Enter starting node for DFS: "))
        result=g.dfs_traversal(start)
        print(f"DFS traversal :{result}")

    elif choice == 4:
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")

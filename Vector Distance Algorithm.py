class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u,v,w):
        self.graph.append([u,v,w])

    def printArr(self,dist):
        print("Vertices \t Distance from the source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))

    def Bellmanford(self, src):
        dist = [float('inf')]*self.V
        dist[src] = 0
        for _ in range(self.V):
            for u,v,w in self.graph: 
                if dist[u] != float('inf') and dist[u]+w < dist[v]:
                    dist[v] = dist[u] + w
        self.printArr(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.Bellmanford(0)

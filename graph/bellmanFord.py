from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellmanFord(self, src):
        dist = [float("inf")] * self.V
        parent = [-1] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for (u, v, w) in self.graph:
                if dist[u] != float("inf") and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parent[v] = u

        # last iteration
        for (u, v, w) in self.graph:
            if dist[u] != float("inf") and dist[v] > dist[u] + w:
                print("negative weight cycle at {} {}".format(u, v))

        self.printArr(dist)

    def printArr(self, dist):
        print("Vertex\t\tDistance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -4)

# Print the solution
g.bellmanFord(0)

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == None:
            return i
        return self.find(parent, parent[i])

    def union(self, x, y, parent, rank):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[y_root] < rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root
            y_root += 1

    def kruskals(self):
        result = []

        parent = [None] * self.V
        rank = [0] * self.V
        i = 0;
        self.graph = sorted(self.graph, key=lambda x: x[2])

        while len(result) < self.V - 1:
            edge = self.graph[i]
            u, v, w = edge
            x_root = self.find(parent, u)
            y_root = self.find(parent, v)
            if x_root != y_root:
                self.union(x_root, y_root, parent, rank)
                result.append(edge)
            i += 1
        self.printTree(result)

    def printTree(self, result):
        for (u, v, w) in result:
            print("{}-{} {}".format(u, v, w))


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
# print(g.graph)
g.kruskals()

from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.V = v
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def isAdjacent(self, u, v):
        for vertice in self.g[u]:
            if vertice == v:
                return True
        return False

    def hamiltonUtil(self, path, u):
        path.append(u)
        print('adding', u)
        for v in range(0, self.V):
            print(v, end=" ")
            if v in path:
                continue
            if self.isAdjacent(u, v):
                print("")
                return self.hamiltonUtil(path, v)

        if len(path) == self.V and self.isAdjacent(path[-1], path[0]):
            return True

        return False

    def isHamilton(self):
        path = []
        isHamilton = self.hamiltonUtil(path, 0)
        print(isHamilton)
        print(path)


g2 = Graph(5)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 4)
g2.addEdge(4, 1)
g2.addEdge(1, 3)
g2.addEdge(3, 0)
g2.addEdge(4, 3)
g2.isHamilton()

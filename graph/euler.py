from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfsUtil(self, u, visited):
        visited[u] = True
        for v in self.g[u]:
            if visited[v] == False:
                self.dfsUtil(v, visited)

    def isConnected(self):
        # graph with no edges, jsut vertices is euler
        visited = [False] * self.V

        for i in range(self.V):
            if len(self.g[i]) >= 1:
                break;

        if i == self.V - 1:
            return True

        self.dfsUtil(i, visited)

        for i in range(self.V):
            if visited[i] == False and len(self.g[i]) > 0:
                return False

        return True

    # 0 not euler, 1 euler path, 2 euler ckt
    def isEulerian(self):
        if self.isConnected() == False:
            return 0

        odd = 0
        for i in range(self.V):
            if len(self.g[i]) % 2 != 0:
                odd += 1
        if odd > 2:
            return 0
        elif odd == 2:
            return 1
        elif odd == 0:
            return 2

    def test(self):
        res = self.isEulerian()
        if res == 0:
            print("graph is not Eulerian")

        elif res == 1:
            print("graph has a Euler path")

        else:
            print("graph has a Euler cycle")


g1 = Graph(5);
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.test()

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
g2.test();

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
g3.test()

# Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
g4.test()

# Let us create a graph with all veritces
# with zero degree
g5 = Graph(3)
g5.test()

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)

    def dfsUtil1(self, u, visited, stack):
        visited[u] = True
        for v in self.g[u]:
            if not visited[v]:
                self.dfsUtil1(v, visited, stack)
        stack.append(u)

    def dfsUtil2(self, u, visited):
        visited[u] = True
        print(u, end=" ")
        for v in self.g[u]:
            if not visited[v]:
                self.dfsUtil2(v, visited)

    def transpose(self):
        gT = Graph(self.V)
        for i in self.g:
            for j in self.g[i]:
                gT.addEdge(j, i)
        return gT

    def printscc(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.dfsUtil1(i, visited, stack)

        gT = self.transpose()

        visited = [False] * self.V
        while stack:
            u = stack.pop()
            if visited[u] == False:
                gT.dfsUtil2(u, visited)
                print("\n")


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components " +
      "in given graph")
g.printscc()

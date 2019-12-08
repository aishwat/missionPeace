from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, s, visited):
        print(s, end=" ")
        visited[s] = True
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfs(i, visited)


g = Graph()
g.addEdge(0, 0)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)
g.addEdge(6, 6)
g.bfs(1)
print("\n")

visited = [False] * len(g.graph)
g.dfs(1, visited)

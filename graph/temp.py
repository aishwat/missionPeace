from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.g = defaultdict(list)
    def addEdge(self, u, v):
        self.g[u].append(v)

    def bfs(self, s):
        visited = [False]*len(self.g)
        q = []

        q.append(s)
        while q:
            s = q.pop()
            print(s)

            for v in self.g[s]:
                if visited[v] == False:
                    q.append(v)
                    visited[v] = True



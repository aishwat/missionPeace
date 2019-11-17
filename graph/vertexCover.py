from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.V = v
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def vertex_cover(self):
        vc = []
        visited = [False] * self.V


        for u in range(self.V):
            if visited[u] == False:
                vc.append(u)

                for v in self.g[u]:
                    if visited[v] == False:
                        visited[u] = True
                        visited[v] = True
                        break;
        print(visited)
        print(vc)

#2 approximate solution,
g = Graph(5)
g.addEdge(0, 2)
g.addEdge(2, 4)
g.addEdge(1, 4)
g.addEdge(3, 4)
g.vertex_cover()
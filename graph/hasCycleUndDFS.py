from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)
        
    def has_cycle(self):
        visited = set()
        for vertex in range(self.V):
            if vertex not in visited:
                flag = self.has_cycle_util(vertex, visited, None)
            if flag:
                return True
        return False

    def has_cycle_util(self, vertex, visited, parent):
        visited.add(vertex)
        # print(self.graph[vertex])
        for adj_vertex in self.graph[vertex]:
            if adj_vertex == parent:
                continue
            if adj_vertex in visited:  # not parent and somehow this vertex is visited, must be by other path
                # so this vertex reachable by 2 paths
                return True
            flag = self.has_cycle_util(adj_vertex, visited, vertex)
            if flag:
                return True
        return False


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.has_cycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1.has_cycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

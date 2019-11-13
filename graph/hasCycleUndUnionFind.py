from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, i, parent):
        if parent[i] == -1:
            return i
        return self.find_parent(parent[i], parent)

    def union(self, x, y, parent):
        x_set = self.find_parent(x, parent)
        y_set = self.find_parent(y, parent)
        parent[x_set] = y_set

    def has_cycle(self):
        parent = [-1] * self.V
        for x in self.graph:
            for y in self.graph[x]:
                x_parent = self.find_parent(x, parent)
                y_parent = self.find_parent(y, parent)
                if x_parent == y_parent:  # 2 vertices represented by same set, so there's already an edge connectiong then
                    # now we have another edge too, so cycle
                    return True
                self.union(x_parent, y_parent, parent)


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.has_cycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

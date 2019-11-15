from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            # print(self.graph)
            if visited[i] == False:
                self.dfs(i, visited, stack)
        return stack

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True

        for adj in self.graph[vertex]:
            if visited[adj] == False:
                self.dfs(adj, visited, stack)

        stack.insert(0, vertex)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
print(g.graph)
stack = g.topological_sort()
print(stack)

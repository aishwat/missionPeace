from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        # self.graph = []
        self.graph = defaultdict(lambda: defaultdict(list))

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

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

        for adj in list(self.graph[vertex].keys()):
            if visited[adj] == False:
                self.dfs(adj, visited, stack)

        stack.insert(0, vertex)

    def longestPath(self, src, stack_):
        dist = [float("inf")] * self.V
        dist[src] = 0

        while stack_:
            u = stack_.pop()
            print(u)
            if dist[u] != float('inf'):
                for v in self.graph[u]:
                    print(v, end=" ")
                    if self.graph[u][v] and self.graph[u][v] and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
                print("\n")
        print(dist)


g = Graph(4)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)

print(g.graph)
# g.addEdge(3, 2, 2)
stack = g.topological_sort()
stack = stack[::-1]
print(stack)
g.longestPath(0, stack)
# print(stack)

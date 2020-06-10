from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)


# Basically all DFS paths

def getHamiltonPaths(N, g, u, visited, paths):
    # if path has N vertices and all diff, it's a hamilton path
    # print("visiting", u)
    visited[u] = True
    paths.append(u)

    if len(paths) == N and len(set(paths)) == N:
        print("===============")
        print(paths)
        return True

    for v in g[u]:
        if not visited[v]:
            getHamiltonPaths(N, g, v, visited, paths)
            # backtrack in for , not out of for
            # this dfs explored, now unvisit this, remove from paths
            # so that this vertex can be used for another exploration
            # print("  backtracking", v)
            visited[v] = False
            paths.pop()


N = 4

edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
graph = Graph(N)

for edge in edges:
    graph.addEdge(edge[0], edge[1])

visited = [False] * 4
print(graph.g)
getHamiltonPaths(N, graph.g, 0, visited, [])
# visited = [False] * 4
# getHamiltonPaths(N, graph.g, 1, visited, [])

# edmonds karp variation
from collections import defaultdict
import queue


class Graph:
    def __init__(self, v):
        self.graph = defaultdict(lambda: defaultdict(list))
        self.V = v

    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = 0


def bfs(g, src, dst):
    hasPath = False
    visited = [False] * len(g)
    queue = []
    parentMap = {}

    queue.append(src)
    visited[src] = True

    while queue:
        u = queue.pop(0)
        # print(u, end = " ")
        if (u == dst):
            hasPath = True
            break

        for v in list(g[u].keys()):
            if visited[v] == False and g[u][v] > 0:
                visited[v] = True
                parentMap[v] = u
                queue.append(v)
    return hasPath, parentMap


def getPath(parent, src, dst):
    # parent is , vertex: got_introduced_by
    path = []

    next = dst
    while next != src:
        path.append(next)
        next = parent[next]
    path.append(src)
    path.reverse()
    return path


def printPath(g, path):
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        print(u, "(", g[u][v], ")", v, end="->")
    print()


def getFlow(g, path):
    weights = []

    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        # print(u, v, " ", g[u][v])
        weights.append(g[u][v])
    return min(weights)


def balanceFlow(g, path, flow):
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        g[u][v] -= flow
        g[v][u] += flow


def FF(g, src, dst):
    hasPath, parentMap = bfs(g.graph, src, dst)
    maxFlow = 0
    while hasPath:
        path = getPath(parentMap, src, dst)
        # print(path)
        printPath(g.graph, path)

        flow = getFlow(g.graph, path)
        print('flow:', flow)
        if flow <= 0:
            break
        maxFlow += flow

        balanceFlow(g.graph, path, flow)
        printPath(g.graph, path)
        print("-------")
        hasPath, parentMap = bfs(g.graph, src, dst)
    print('maxFlow', maxFlow)


g = Graph(7)
g.addEdge(0, 0, 0)
g.addEdge(1, 2, 3)
g.addEdge(1, 4, 3)

g.addEdge(2, 3, 4)

g.addEdge(3, 1, 3)
g.addEdge(3, 4, 1)
g.addEdge(3, 5, 2)

g.addEdge(4, 5, 2)
g.addEdge(4, 6, 6)

g.addEdge(5, 2, 1)
g.addEdge(5, 7, 1)

g.addEdge(6, 7, 9)

g.addEdge(7, 7, 0)

src = 1
dst = 7
FF(g, src, dst)

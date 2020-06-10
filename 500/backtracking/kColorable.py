from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)


colors = ["", "BLUE", "GREEN", "RED", "YELLOW",
          "ORANGE", "PINK", "BLACK", "BROWN", "WHITE", "PURPLE"]


def isSafe(g, color, u, colorConfig):
    # if any adj vertice has this color then its not safe
    for v in g[u]:
        if colorConfig[v] == color:
            return False
    return True


def getColorConfigs(N, K, g, u, colorConfig):
    if len(colorConfig) == N:
        print(colorConfig)
        return True

    for color in colors:
        if isSafe(g, color, u, colorConfig):
            colorConfig[u] = color
            for v in g[u]:
                getColorConfigs(N, K, g, v, colorConfig)
                colorConfig[u] = ""


N = 6
K = 3  # Max number of colors allowed
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
graph = Graph(N)

for edge in edges:
    graph.addEdge(edge[0], edge[1])

colorConfig = [] * N
print(graph.g)
getColorConfigs(N, K, graph.g, 0, colorConfig)

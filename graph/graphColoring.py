from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.V = v;
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def getColoring(self):
        result = [-1] * self.V
        # available = [True] * self.V
        result[0] = 0

        for u in range(1, self.V):
            available = [True] * self.V
            # find available colors, if adj has color, that's not available
            for v in self.g[u]:
                if result[v] != -1:
                    available[result[v]] = False  # not available[v] = False
            for i in range(self.V):
                if available[i] == True:
                    break;
            result[u] = i;
        print(result)


g1 = Graph(5);
g1.addEdge(0, 1);
g1.addEdge(0, 2);
g1.addEdge(1, 2);
g1.addEdge(1, 3);
g1.addEdge(2, 3);
g1.addEdge(3, 4);
g1.getColoring();

g2 = Graph(5);
g2.addEdge(0, 1);
g2.addEdge(0, 2);
g2.addEdge(1, 2);
g2.addEdge(1, 4);
g2.addEdge(2, 4);
g2.addEdge(4, 3);
g2.getColoring();

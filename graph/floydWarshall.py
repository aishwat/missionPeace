INF = float('inf')


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def floydWarshall(self):
        dist = [row[:] for row in self.graph]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf') and \
                            dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(self.V):
            for j in range(self.V):
                print(dist[i][j], end="\t")
            print("\n")


g = Graph(4)
g.graph = [[0, 5, INF, 10],
           [INF, 0, 3, INF],
           [INF, INF, 0, 1],
           [INF, INF, INF, 0]
           ]
# Print the solution
g.floydWarshall();

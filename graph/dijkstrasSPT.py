# 3 things, key(dist), mstSet(ssptSet), parent

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def minKey(self, dist, sptSet):
        min = float("inf")
        min_index = None
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        parent = [None] * self.V
        dist = [float("inf")] * self.V
        sptSet = [False] * self.V
        dist[src] = 0
        parent[src] = -1

        for count in range(self.V):
            u = self.minKey(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                # if connected, in mst, key greater than edge connection
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > self.graph[u][v] + dist[u]:
                    dist[v] = self.graph[u][v] + dist[u]
                    parent[v] = u
        self.printDist(parent, dist)

    def printDist(self, parent, dist):
        for i in range(0, self.V):
            print(i, " ", dist[i])
        # print('Edge \tWeight')
        # for i in range(1, self.V):
        #     print("{}-{} \t{}".format(parent[i], str(i), self.graph[parent[i]][i]))


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);

# import heapq


# class PQNode:
#
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#
#     # compares the second value
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __str__(self):
#         return str("{} : {}".format(self.key, self.value))
#
#
# input = [PQNode(1, 4), PQNode(7, 4), PQNode(6, 9), PQNode(2, 5)]

# hinput = []
# for item in input:
#     heapq.heappush(hinput, item)
#
# while (hinput):
#     print(heapq.heappop(hinput))

# 3 things, key, mstSet, parent

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def minKey(self, key, mstSet):
        min = float("inf")
        min_index = None
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prims(self):
        parent = [None] * self.V
        key = [float("inf")] * self.V
        mstSet = [False] * self.V
        key[0] = 0
        parent[0] = -1

        for count in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                # if connected, in mst, key greater than edge connection
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

    def printMST(self, parent):
        print('Edge \tWeight')
        for i in range(1, self.V):
            print("{}-{} \t{}".format(parent[i], str(i), self.graph[parent[i]][i]))


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.prims()

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

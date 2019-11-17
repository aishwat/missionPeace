from collections import defaultdict


class Graph:
    def __init__(self, row, col, g):
        self.R = row
        self.C = col
        self.g = g

    def isSafeToVisit(self, i, j, visited):
        if i >= 0 and i < self.R and j >= 0 and j < self.C and visited[i][j] == False and self.g[i][j] == 1:
            return True

    def dfsUtil(self, i, j, visited):
        visited[i][j] = True
        if self.isSafeToVisit(i - 1, j - 1, visited):
            self.dfsUtil(i - 1, j - 1, visited)
        if self.isSafeToVisit(i - 1, j, visited):
            self.dfsUtil(i - 1, j, visited)
        if self.isSafeToVisit(i - 1, j + 1, visited):
            self.dfsUtil(i - 1, j + 1, visited)

        if self.isSafeToVisit(i, j - 1, visited):
            self.dfsUtil(i, j - 1, visited)
        if self.isSafeToVisit(i, j + 1, visited):
            self.dfsUtil(i, j + 1, visited)

        if self.isSafeToVisit(i + 1, j - 1, visited):
            self.dfsUtil(i + 1, j - 1, visited)
        if self.isSafeToVisit(i + 1, j, visited):
            self.dfsUtil(i + 1, j, visited)
        if self.isSafeToVisit(i + 1, j + 1, visited):
            self.dfsUtil(i + 1, j + 1, visited)

    def countIslands(self):
        visited = [[False for col in range(self.C)] for R in range(self.R)]

        count = 0;
        for i in range(self.R):
            for j in range(self.C):
                if visited[i][j] == False and self.g[i][j] == 1:
                    self.dfsUtil(i, j, visited)
                    count += 1
        return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:")

print(g.countIslands())

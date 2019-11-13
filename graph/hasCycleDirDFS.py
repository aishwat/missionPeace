from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.parent_map = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def hasCycle(self):
        white_set = set()
        gray_set = set()
        black_set = set()

        for vertex in self.graph:
            white_set.add(vertex)

        while white_set is not None:
            vertex = white_set.pop()
            flag = self.dfs(vertex, white_set, gray_set, black_set)
            if flag:
                return True
        return False

    def dfs(self, vertex, white_set, gray_set, black_set):
        self.move(vertex, white_set, gray_set)

        for adj in self.graph[vertex]:
            self.parent_map[adj] = vertex
            if adj in black_set:
                continue;
            if adj in gray_set:
                return True
            flag = self.dfs(adj, white_set, gray_set, black_set)
            if flag:
                return True
        self.move(vertex, gray_set, black_set)
        return False

    def move(self, vertex, set1, set2):
        if vertex in set1:
            set1.remove(vertex)
        set2.add(vertex)


graph = Graph(6)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(4, 1)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 4)

print(graph.hasCycle())
print(graph.parent_map)

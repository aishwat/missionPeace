from typing import List
from treeUtils import TreeNode, Tree
import heapq
import re
import functools
from collections import defaultdict, deque, Counter, OrderedDict
import json
from linkedListUtil import LinkedList, ListNode
import bisect
import math
from collections import defaultdict, OrderedDict, Counter
import string
import itertools
from functools import cmp_to_key
import itertools


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        cycle = False

        for i in range(m):
            if cycle:
                return True
            for j in range(n):
                if not visited[i][j]:
                    cycle = self.dfs(i, j, m, n, visited, grid, -1, -1)
                if cycle:
                    return True
        return False

    def dfs(self, i, j, m, n, visited, grid, parent_x, parent_y):
        visited[i][j] = True

        R = [0, 0, -1, 1]
        C = [1, -1, 0, 0]
        for r, c in zip(R, C):
            x = i + r
            y = j + c

            if 0 <= x < m and 0 <= y < n and (x, y) and grid[x][y] == grid[i][j] and not (
                    x == parent_x and y == parent_y):
                if visited[x][y]:
                    return True
                else:
                    check = self.dfs(x, y, m, n, visited, grid, i, j)
                    if check:
                        return True
        return False


s = Solution()
grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
grid = [["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]
grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
grid = [["f", "a", "a", "c", "b"],
        ["e", "a", "a", "e", "c"],
        ["c", "f", "b", "b", "b"],
        ["c", "e", "a", "b", "e"],
        ["f", "e", "f", "b", "f"]]
print(s.containsCycle(grid))
#
#
# def containsCycle(self, grid: List[List[str]]) -> bool:
#     m, n = len(grid), len(grid[0])
#
#     for i in range(m):
#         for j in range(n):
#             self.src = (i, j)
#             self.hasCycle = False
#             self.dfs(i, j, m, n, grid, [], [])
#             if self.hasCycle:
#                 return True
#     return False
#
#
# def dfs(self, i, j, m, n, grid, path, res):
#     if len(path) >= 4 and self.src == path[-1]:
#         self.hasCycle = True
#         return
#
#     R = [0, 0, -1, 1]
#     C = [1, -1, 0, 0]
#     for r, c in zip(R, C):
#         x = i + r
#         y = j + c
#
#         if 0 <= x < m and 0 <= y < n and (x, y) not in path and grid[x][y] == grid[i][j]:
#             self.dfs(x, y, m, n, grid, path + [(x, y)], res)

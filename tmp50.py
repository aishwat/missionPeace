from typing import List, Optional
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
import random
import hashlib
from collections import Counter

import math
import os
import random
import re
import sys


# Find missing lowest positive number
# LCA

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                [x1, y1] = points[i]
                [x2, y2] = points[j]
                dist[i][j] = abs(x1 - x2) + abs(y1 - y2)
        for row in dist:
            print(row)

        cost = [float('INF') for _ in range(n)]
        cost[0] = 0

        for i in range(n):
            for j in range(i + 1, n):
                cost[j] = min(cost[j], cost[i] + dist[i][j])
                print(i, j, cost[j])
        print(cost)


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
Solution().minCostConnectPoints(points)

from typing import List, Optional
from treeUtils import TreeNode, Tree
import heapq, re, functools, json
from collections import defaultdict, deque, Counter, OrderedDict, defaultdict, OrderedDict, Counter
from linkedListUtil import LinkedList, ListNode
import bisect, math, string, itertools
from functools import cmp_to_key
import itertools, random, hashlib, os, sys


class Solution:
    def uniquePathsWithObstacles(self, dp: List[List[int]]) -> int:
        rows, cols = len(dp), len(dp[0])
        if dp[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1, rows):
            dp[i][0] = 1 if (dp[i][0] == 0 and dp[i - 1][0] == 1) else 0
        for j in range(1, cols):
            dp[0][j] = 1 if (dp[0][j] == 0 and dp[0][j - 1] == 1) else 0
        for i in range(1, rows):
            for j in range(1, cols):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        print(dp)
        return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

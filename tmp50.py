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


class Solution:
    def nextGreater(self, a):
        # nextgreater = [len(a)] * len(a)
        # for i in range(len(a) - 2, -1, -1):
        #     p = i + 1
        #     while p < len(a) and a[p] < a[i]:
        #         # p += 1
        #         p = nextgreater[p]
        #     nextgreater[i] = p
        # print(nextgreater)

        nextgreater = [len(a)] * len(a)
        s = []
        for i in range(len(a) - 1, -1, -1):
            while len(s) and a[i] > s[-1]:
                s.pop()
            if len(s):
                nextgreater[i] = s[-1]
            s.append(a[i])
            print(s)

        print(nextgreater)


a = [4, 5, 2, 25]
a = [13, 7, 6, 12]
# a = [11, 13, 21, 3]
print(Solution().nextGreater(a))

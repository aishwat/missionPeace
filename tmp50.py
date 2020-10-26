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
import random


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dfs(root, [], [])

    def dfs(self, root, path, res):

        if not root.left and root.right:
            print(path + [root.val])
        if root.left:
            self.dfs(root.left, path + [root.val], res)
        if root.right:
            self.dfs(root.right, path + [root.val], res)


a = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
tree = Tree(a)
print(Solution().maxAncestorDiff(tree.root))

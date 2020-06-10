def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    if n == 1:
        return s

    T = [[1 for i in range(n)] for j in range(n)]

    maxi = 0
    maxL = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            T[i][i + 1] = 2
            maxi = i
            maxL = 1


    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l
            # print(i, j)

            if s[i] == s[j] and T[i + 1][j - 1] == l - 1:
                T[i][j] = T[i + 1][j - 1] + 2
                maxi = i
                maxL = max(maxL, l)
            else:
                T[i][j] = max(T[i + 1][j], T[i][j - 1])

    print(s[maxi:maxi + maxL+1])
    # print(maxL)

    # for i in range(n):
    #     for j in range(n):
            # print(T[i][j], end=" ")
        # print()


longestPalindrome("abbcd")
# import math
# INF = math.inf
#
# def findMedianSortedArrays( nums1: [int], nums2: [int]) -> float:
#     if len(nums1) > len(nums2):
#         return findMedianSortedArrays(nums2, nums1)
#     x, y = len(nums1), len(nums2)
#
#     lo = 0
#     hi = x
#     while (lo <= hi):
#         # print()
#         # print(lo,hi)
#         px = (lo + hi) // 2
#         py = ((x + y + 1) // 2) - px
#         print(px, py)
#         # maxLeftX, minRightX
#         maxLeftX = -INF if px == 0 else nums1[px - 1]
#         minRightX = INF if px == x else nums1[px]
#
#         # maxLeftY, minRightY
#         maxLeftY = -INF if py == 0 else nums2[py - 1]
#         minRightY = INF if py == y else nums2[py]
#
#         print(maxLeftX, minRightY)
#         print(maxLeftY, minRightX)
#         if (maxLeftX <= minRightY and maxLeftY <= minRightX):
#             if (x + y) % 2 == 0:
#                 return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
#             else:
#                 return max(maxLeftX, maxLeftY)
#         elif maxLeftX > minRightY:
#             hi = px - 1
#         else:
#             lo = px + 1
#
#
# print( findMedianSortedArrays([100000], [100001]))
# def SmallestSubString(S):
#     # Write your code here
#     max_len = 0
#     max_ij = ()
#     n = len(S)
#     T = [[0 for i in range(n + 1)] for j in range(n + 1)]
#     for i in range(0, n):
#         T[i][i] = 1
#
#     for l in range(1, n):
#         for i in range(0, n - l):
#             j = i + l
#
#             if S[j] in S[i:j]:
#                 print("test")
#                 T[i][j] = max(T[i + 1][j], T[i][j - 1])
#             else:
#                 T[i][j] = min(T[i + 1][j], T[i][j - 1])+1
#             print(i, j, T[i][j])
#     for i in range(0, n):
#         for j in range(0, n):
#             print(T[i][j], end=" ")
#         print()
#
#
# S = "aabcdb"
#
# out_ = SmallestSubString(S)
# print(out_)

# def SmallestSubString(S):
#     # Write your code here
#     max_len = 0
#     max_ij = ()
#     n = len(S)
#     T = [[0 for i in range(n + 1)] for j in range(n + 1)]
#     for l in range(0, n):
#         for i in range(0, n - l):
#             j = i + l
#
#             _set = set(S[i:j + 1])
#             print(i, j, len(_set))
#             T[i][j] = len(_set)
#             if max_len < len(_set):
#                 max_len = len(_set)
#                 max_ij = (i, j)
#             # for k in range(i, j):
#             #     print(i,j)
#     print(max_len, max_ij)
#     for i in range(0, n):
#         for j in range(0, n):
#             print(T[i][j], end=" ")
#         print()
#     return max_ij[1]-max_ij[0]+1
#
#
# S = "aabcdbfgtx"
#
# out_ = SmallestSubString(S)
# print(out_)

# def finalPrice(prices):
#     # Write your code here
#     n = len(prices)
#     sum = 0
#     fullPriced = []
#
#     min_right = min(prices[0:n])
#     for i in range(n - 1):
#         # min_right = min(prices[i+1:n])
#         if min_right < prices[i]:
#             sum += prices[i] - min_right
#         else:
#             fullPriced.append(i)
#             min_right = min(prices[i + 1:n])
#             sum += prices[i]
#
#     sum += prices[n - 1]
#     fullPriced.append(n - 1)
#     fullPriced = [str(price) for price in fullPriced]
#     print(sum)
#     print(" ".join(fullPriced))
#
#
# print(finalPrice([1, 3, 3, 2, 5]))
# # !/bin/python
#
#
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'lastStoneWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY weights as parameter.
#
# import heapq
#
#
# def lastStoneWeight(weights):
#     # n = len(weights)
#
#     # heapq._heapify_max(weights)
#
#     if len(weights) == 0:
#         return 0
#     if len(weights) == 1:
#         return weights[0]
#     while (weights):
#         # print(weights)
#         heapq._heapify_max(weights)
#         wt1 = heapq._heappop_max(weights)
#         wt2 = heapq._heappop_max(weights)
#         # print(wt1, wt2)
#         if (wt1 == wt2):
#             continue;
#         elif wt1 > wt2:
#             # print(wt1 - wt2)
#             heapq.heappush(weights, wt1 - wt2)
#         else:
#             heapq.heappush(weights, -wt1 + wt2)
#
#         # odd count
#         if len(weights) == 1:
#             return weights[0]
#     return 0
#
#     # Write your code here
#
#
# print(lastStoneWeight([46188086,
#                        339992587,
#                        742976890,
#                        801915058,
#                        393898202,
#                        717833291,
#                        843435009,
#                        361066046,
#                        884145908,
#                        668431192,
#                        586679703,
#                        792103686,
#                        85425451,
#                        246993674,
#                        134274127,
#                        586374055,
#                        923288873,
#                        292845117,
#                        399188845,
#                        842456591,
#                        410257930,
#                        333998862,
#                        16561419,
#                        624279391,
#                        459765367,
#                        969764608,
#                        508221973,
#                        82956997,
#                        437034793,
#                        553121267,
#                        554066040,
#                        199416087,
#                        ]))
# def isSafe(row, col, rows, columns):
#     if 0 <= row < rows and 0 <= col < columns:
#         return True
#     else:
#         return False
#
#
# def isAllOne(rows, columns, grid):
#     for i in range(rows):
#         for j in range(columns):
#             if grid[i][j] == 0:
#                 return False
#     return True
#
#
# def minimumDays(rows, columns, grid):
#     print(rows, columns)
#     # WRITE YOUR CODE HERE
#     _r = [-1, 0, 1, 0]
#     _c = [0, 1, 0, -1]
#
#     count = 0
#     for c in range(rows):
#         visited = [[False for j in range(columns)] for i in range(rows)]
#         for i in range(rows):
#             for j in range(columns):
#                 for k in range(4):
#                     adj_row = i + _r[k]
#                     adj_col = j + _c[k]
#                     if grid[i][j] == 1 and isSafe(adj_row, adj_col, rows, columns) and grid[adj_row][adj_col] == 0 and \
#                             visited[i][j] == False:
#                         visited[i][j] = True  # now for this all adjacents are visited
#                         grid[adj_row][adj_col] = 1
#                         visited[adj_row][adj_col] = True
#                         # can break here
#         count += 1
#         if isAllOne(rows, columns, grid):
#             print(count)
#             break
#     return count
#
#
# T = [[1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 0],
#      [0, 0, 0, 0, 1]]
# minimumDays(5, 5, T)
#
# # def minimumDays(rows, columns, grid):
# #     if not rows or not columns:
# #         return 0
# #
# #     q = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j] == 1]
# #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# #     time = 0
# #
# #     print(q)
# #     while True:
# #         new = []
# #         for [i, j] in q:
# #             for d in directions:
# #                 ni, nj = i + d[0], j + d[1]
# #                 if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
# #                     grid[ni][nj] = 1
# #                     new.append([ni, nj])
# #         print(new)
# #         q = new
# #         if not q:
# #             break
# #         time += 1
# #
# #     return time
# #
# # T = [[1, 0, 0, 0, 0],
# #      [0, 1, 0, 0, 0],
# #      [0, 0, 1, 0, 0],
# #      [0, 0, 0, 1, 0],
# #      [0, 0, 0, 0, 1]]
# # print(minimumDays(5, 5, T))
# # from collections import Counter
# #
# #
# # def topNCompetitors(reviews, topNCompetitors, competitors):
# #     words = []
# #     for i in range(len(reviews)):
# #         tmp = reviews[i].split(" ")
# #         words.extend(list(set(tmp)))
# #     wordDict = Counter(words)
# #
# #     filteredDict = {}
# #     for key, cnts in list(wordDict.items()):
# #         if key in competitors:
# #             filteredDict[key] = wordDict[key]
# #     print(filteredDict)
# #
# #     topN = [k for k, v in sorted(filteredDict.items(), key=lambda item: item[1], reverse=True)]
# #     print(topN)
# #     topN = [item for item in sorted(topN)]
# #     return topN[:topNCompetitors]
# #
# #
# # topNCompetitors(["some some dumb review", "another review", "], 2, ["dumb"])
#
# # #!/bin/python3
# #
# # import math
# # import os
# # import random
# # import re
# # import sys
# #
# #
# # #
# # # Complete the 'fetchItemsToDisplay' function below.
# # #
# # # The function is expected to return a STRING_ARRAY.
# # # The function accepts following parameters:
# # #  1. 2D_STRING_ARRAY items
# # #  2. INTEGER sortParameter
# # #  3. INTEGER sortOrder
# # #  4. INTEGER itemPerPage
# # #  5. INTEGER pageNumber
# # #
# # class Item:
# #     def __init__(self, name, relevance, price):
# #         self.name = name
# #         self.relevance = relevance
# #         self.price = price
# #
# #     def __repr__(self):
# #         return self.name + " " + self.relevance + " " + self.price
# #
# #
# # from functools import partial
# #
# #
# # def sort_key(sortParameter, item):
# #     print(item[sortParameter])
# #     return item[sortParameter]
# #
# #
# # def fetchItemsToDisplay(items, sortParameter, sortOrder, itemPerPage, pageNumber):
# #     # sortedItems = sorted(items, key=lambda item: order * int(item[sortParameter]))
# #     bound_sort_key = partial(sort_key, sortParameter)
# #     sortedItems = sorted(items, key=bound_sort_key, reverse=sortOrder == 1)
# #     print(sortedItems)
# #     #
# #     # start = pageNumber * itemPerPage
# #     # end = (pageNumber + 1) * itemPerPage
# #     # sorted_items_on_page = sortedItems[start:end]
# #     # names = [item[0] for item in sorted_items_on_page]
# #     # print(names)
# #     # return names
# #
# #
# # fetchItemsToDisplay([["owjevtkuyv", "58584272", "62930912"], ["rpaqgbjxik", "9425650", "96088250"],
# #                      ["dfbkasyqcn", "37469674", "46363902"], ["vjrrisdfxe", "18666489", "88046739"]], 0, 1, 2, 0)
# #
# # # if __name__ == '__main__':
# #
# #
# # # # Python Implementation of above approach
# # #
# # # import collections
# # #
# # #
# # # # function to find minimum increment required
# # # def minIncrementForUnique(A):
# # #     # collect frequency of each element
# # #     count = collections.Counter(A)
# # #     print(count)
# # #
# # #     # array of unique values taken
# # #     taken = []
# # #
# # #     ans = 0
# # #
# # #     for x in range(20):
# # #
# # #         if count[x] >= 2:
# # #             taken.extend([x] * (count[x] - 1))
# # #         elif taken and count[x] == 0:
# # #             tmp = x - taken.pop()
# # #             print(tmp)
# # #             ans += tmp
# # #
# # #         print(x, count[x], taken)
# # #
# # #     # return answer
# # #     return ans
# # #
# # #
# # # # Driver code
# # # A = [3, 2, 1, 2, 1, 7]
# # # print(minIncrementForUnique(A))
# #
# # # def isPalindrome(s):
# # #     n = len(s)
# # #     for i in range(n):
# # #         if s[i] != s[n - 1 - i]:
# # #             return False
# # #     return True
# # #
# # #
# # # # print(isPalindrome("a"))
# # #
# # #
# # # #
# # # def shortestPalindrome(s):
# # #     # Write your code here
# # #     n = len(s)
# # #     count = 0
# # #     for i in range(n+1):
# # #         # print(s[:i])
# # #         if isPalindrome(s[:i]):
# # #             count = 0
# # #         else:
# # #             count += 1
# # #     print(count)
# # #     return count
# # #
# # # def getMisMatch(s):
# # #     n = len(s)
# # #     count = 0
# # #     for i in range((n + 1)//2):
# # #         # print(s[:i])
# # #         if isPalindrome(s[:i]):
# # #             count = 0
# # #         else:
# # #             count += 2
# # #     # print(count)
# # #     return count
# # #
# # #
# # # getMisMatch("abcda")
# # #
# # # def shortestPalindrome(s):
# # #     n = len(s)
# # #     T = [[0 for i in range(n)] for j in range(n)]
# # #
# # #     for l in range(2, n + 1):
# # #         for i in range(0, n - l + 1):
# # #             j = i + l - 1
# # #             print(s[i], s[j], end="")
# # #             if s[i] == s[j]:
# # #                 T[i][j] = T[i + 1][j - 1]
# # #             else:
# # #                 T[i][j] = max(T[i - 1][j], T[i][j - 1]) + 1
# # #
# # #             print(T[i][j])
# # #     for i in range(n):
# # #         for j in range(n):
# # #             print(T[i][j], end=" ")
# # #         print()
# # #
# # #
# # # shortestPalindrome("abcda")
# #
# # #
# # # def display_arguments(func):
# # #     def display_and_call(*args, **kwargs):
# # #         args = list(args)
# # #         print('must-have arguments are:')
# # #         for i in args:
# # #             print(i)
# # #         print('optional arguments are:')
# # #         for kw in kwargs.keys():
# # #             print(kw + '=' + str(kwargs[kw]))
# # #         return func(*args, **kwargs)
# # #
# # #     return display_and_call
# # #
# # #
# # # @display_arguments
# # # def my_add(m1, p1=0):
# # #     output_dict = {}
# # #     output_dict['r1'] = m1 + p1
# # #     return output_dict
# # #
# # #
# # # my_add(4)

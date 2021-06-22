# medium - sorted on frequency, session:Main
# 1041 Robot Bounded In Circle
# 1396 Design Underground System
# 767 Reorganize String
# 443 String Compression
#
# 547. Friend Circles
#
# 445. Add Two Numbers II - linked list
# tricky part is forming a reverse linked list
#
# 1283. Find the Smallest Divisor Given a Threshold
#
# 981	Time Based Key-Value Store - redo
# 1197. Minimum Knight Moves - very tricky
#
# 695. Max Area of Island
#
# 987. Vertical Order Traversal of a Binary Tree <- same as 314
# 609. Find Duplicate File in System
# 362. Design Hit Counter <- revisit
#
# 289. Game of Life - lil dirty trick
# 332. Reconstruct Itinerary <- revisit
#
# 974. Subarray Sums Divisible by K <- revisit
# 1209. Remove All Adjacent Duplicates in String II
# 468. Validate IP Address
# 399. Evaluate Division
#
#
# 526. Beautiful Arrangement <- revisit
#
# 368. Largest Divisible Subset
# 532. K-diff Pairs in an Array <- hidden binary search
#
#
# 529. Minesweeper
# 388. Longest Absolute File Path <- good
#
# 378. Kth Smallest Element in a Sorted Matrix
#
# 1653. Minimum Deletions to Make String Balanced
#
# 395. Longest Substring with At Least K Repeating Characters <- tricky, split on freq
#
#
# 722. Remove Comments
# 1130. Minimum Cost Tree From Leaf Values <- very tricky
# 1472. Design Browser History
#
# 341. Flatten Nested List Iterator <- good, tricky
# 417. Pacific Atlantic Water Flow
#
# 592. Fraction Addition and Subtraction <-  tricky splitting
# def gcd(self, a, b):
#     while b:
#         a, b = a, a % b
#     return a
# lst = expression.replace("+", " +").replace("-", " -").split()

# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# detour 239. Sliding Window Maximum <- template
# use of deque to get max in window of len k, in O(n),
# for max, 1. deque never holds elements less than current num, and so is decreasing, max is dq[0]

# 698 - skipped, hard
# 402. Remove K Digits <- lil trick
# 545. Boundary of Binary Tree <- tricky traversal, lot doesnt work, fails where leaves are at different depths
#
# 393. UTF-8 Validation
# https://stackoverflow.com/questions/699866/python-int-to-binary-string
# instead of "{0:b}".format(d)
# use format(d, '08b') directly <- pads 8 0's
#
# 735. Asteroid Collision <- good use of while else, tricky
# 1344. Angle Between Hands of a Clock
#
# 539. Minimum Time Difference <- good que
# find difference b/w pairs in circular array
# a.append(a[0] + 1440)
# diffs = [y - x for x, y in zip(a, a[1:])]
# https://www.youtube.com/watch?v=-o_YDXNfRUY <- template diag
#
#
# 723. Candy Crush <- implementation heavy

# from sunday round
# 1673. Find the Most Competitive Subsequence
# 1674. Minimum Moves to Make Array Complementary <- very hard
# 1675. Minimize Deviation in Array

# 1010. Pairs of Songs With Total Durations Divisible by 60
#
# 1029. Two City Scheduling
def getMedian(X, Y):
    l1 = len(X)  # l1 is the shorter array
    l2 = len(Y)
    median_index = (l1 + l2 + 1) // 2
    print(median_index)

    for x in range(l1):
        y_ = median_index - x  # this is the number of elements y must have to balance,
        y = y_ - 1  # to get index  //index is bit confusing, write on paper and see
        # xth index is left elem, yth index is right elem
        print(x, y)
        if y - 1 >= 0 and x + 1 < l1 and X[x] < Y[y] and Y[y - 1] < X[x + 1]:
            print("got ", x, y)

# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         n1, n2 = len(nums1), len(nums2)
#         if n1 == 0 and n2 == 0:
#             return 0
#
#         if len(nums1) > len(nums2):
#             return self.findMedianSortedArrays(nums2, nums1)
#
#         l, r = 0, n1
#
#         while l <= r:
#             mid1 = l + r >> 1
#             mid2 = (n1 + n2 + 1) // 2 - mid1
#             print(mid1, mid2)
#
#             l1 = -float("inf") if mid1 == 0 else nums1[mid1 - 1]
#             r1 = float("inf") if mid1 == n1 else nums1[mid1]
#
#             l2 = -float("inf") if mid2 == 0 else nums2[mid2 - 1]
#             r2 = float("inf") if mid2 == n2 else nums2[mid2]
#
#             if l1 <= r2 and l2 <= r1:
#                 if (n1 + n2) % 2 == 0:
#                     return float(max(l1, l2) + min(r1, r2)) / 2
#                 else:
#                     return float(max(l1, l2))
#             elif l1 > r1:
#                 r = mid1 - 1
#             else:
#                 l = mid1 + 1
#         return

getMedian([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])

# # Find the length of smallest subarray whose sum of elements is greater than the given number
# # for practice
# # taking long skip, fixable, come back later
#
# def getSmallestSubArr(a, k):
#     windowSum = 0
#     left = 0
#     minLen = 99
#     minLeft = 0
#
#     for right in range(len(a)):
#         windowSum += a[right]
#
#         if windowSum < k:
#             continue
#         #  maintain window of min size
#         while windowSum > k and left < right:
#             windowSum -= a[left]
#             left += 1
#         windowSum += a[left]  # at exit of while would have gone less than k
#
#         if right - left + 1 < minLen and windowSum > k:
#             print("setting minLen", a[left: right + 1])
#             print(windowSum)
#             minLen = right - left + 1
#             minLeft = left
#     print(a[minLeft:minLeft + minLen + 1])
#
#
# getSmallestSubArr([1, 2, 3, 4, 5, 6, 7, 8], 20)

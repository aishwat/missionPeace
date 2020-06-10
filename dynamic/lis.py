#LONGEST INCREASING SUBSEQUENCE
# def getLIS(a):
#     LIS = [1] * len(a)
#
#     for i in range(1, len(a)):
#         for j in range(0, i):
#             if a[i] > a[j]:
#                 LIS[i] = max(LIS[i], LIS[j] + 1)
#
#     print(LIS)
#

# ------------Onlgn-------------------
def getCeilIndex(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r


def getLIS(a):
    tailTable = [0] * len(a)
    _len = 1

    tailTable[0] = a[0]

    for i in range(1, len(a)):
        print(a[i], tailTable)
        if a[i] < tailTable[0]:
            #never executed
            tailTable[0] = a[i]
        elif a[i] > tailTable[_len - 1]:
            tailTable[_len] = a[i]
            _len += 1
        else:
            ceilIndex = getCeilIndex(tailTable, -1, _len - 1, a[i])
            print('ceil for ', a[i],':', tailTable[ceilIndex])
            tailTable[ceilIndex] = a[i]

    print(_len)
    print(tailTable)
    return tailTable


# a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# a = [3, 4, -1, 0, 6, 2, 3]
# a = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# a = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
# print(a)
# print([a[i] for i in range(len(a))])
indexes = getLIS(a)

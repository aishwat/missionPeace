# Find count of distinct elements in every sub-array of size k
from collections import defaultdict


# something wrong with imnpl, come back, but logic is somwhqta same

def getCounts(a, k):
    countMap = defaultdict(int)
    n = len(a)

    j = 0
    for i in range(0, n):

        if i < k - 1:
            countMap[a[i]] += 1
            print(countMap)
            continue

        if i - j >= k:
            # print(j,i)
            countMap[a[i]] += 1
            countMap[a[j]] -= 1
            print('adding ', a[i])
            print('removing ', a[j])

            uniqueElem = sum(x > 0 for x in list(countMap.values()))
            print(uniqueElem)
            j += 1


getCounts([2, 1, 2, 3, 2, 1, 4, 5], 5)

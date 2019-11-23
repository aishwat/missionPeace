# check-subarray-with-0-sum-exists-not

arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
from collections import defaultdict


def getContSubArrWithSumZero(arr):
    _set = set([0])
    result = []
    sum = 0
    for i in range(len(arr)):
        print(_set)
        sum += arr[i]
        if sum in _set:
            result.append(arr[i])
        else:
            _set.add(sum)
    return result


# not exact but somewhat close
def printContSubArrWithSumZero(arr):
    dict = {0: 0}
    result = []
    sum = 0
    for i in range(len(arr)):
        print(dict)
        sum += arr[i]
        if sum in list(dict.keys()):
            fromIndex = dict.get(sum)
            result.append((fromIndex, i))
        else:
            dict[sum] = i
    return result


# print(getContSubArrWithSumZero(arr))  # gives number of subarrays with sum 0
print(printContSubArrWithSumZero(arr))

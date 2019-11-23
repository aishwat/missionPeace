# Find maximum length sub-array having given sum
# similar concept to check-subarray-with-0-sum-exists-not
#just remember can leverage hashing
def getLen(arr, S):
    sumMap = {0: -1}
    _sum = 0
    _len = 0
    end = -1
    for i in range(len(arr)):
        _sum += arr[i]
        if _sum not in list(sumMap.keys()):
            sumMap[_sum] = i

        if _sum - S in list(sumMap.keys()):
            _len = max(_len, i - sumMap[_sum - S])
            end = i

    print(arr[end - _len: end])


arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
getLen(arr, 8)

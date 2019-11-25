# Find maximum length sub-array having equal number of 0’s and 1’s
# convert 0s to -1 and becomes find sum=0 problem, much like 3

def getMaxLen(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    _sumMap = dict({0: -1})
    _sum = 0
    _len = 0
    ending_index = -1
    for i in range(len(arr)):
        _sum += arr[i]

        if _sum in _sumMap.keys():

            if i - _sumMap[_sum] > _len:
                _len = i - _sumMap[_sum]
                ending_index = i
        if _sum not in _sumMap.keys():
            _sumMap[_sum] = i

    return (_len, ending_index)


arr = [0, 0, 1, 0, 1, 0, 0]
(_len, ending_index) = getMaxLen(arr)
print(arr[ending_index - _len + 1:ending_index + 1])

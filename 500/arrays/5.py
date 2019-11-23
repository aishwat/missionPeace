# Find a duplicate element in a limited range array
# naive approach set/hash. O(n) time O(n) space

# time O(n) space O(1)
# or xor approach
def getSign(a):
    return -(1 if a >= 0 else -1)


def getDuplicate(arr):
    # mark array elements as negative by using array indexes as keys
    for i in range(len(arr)):
        indexToSet = arr[i]
        arr[indexToSet - 1] *= getSign(indexToSet)
    print(arr)
    for i in range(len(arr)):
        if arr[i] >= 0:
            print(arr[i])


getDuplicate([1, 2, 3, 4, 2])

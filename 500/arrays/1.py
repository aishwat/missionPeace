# O(n lgn) to sort and traverse 2 pointers
# O(n) put entries in hash
def pairWithGivenSum(arr, sum):
    _set = set()
    _set.add(arr[0])

    solutions = []
    for i in range(1, len(arr)):
        if sum - arr[i] in _set:
            solutions.append((sum - arr[i], arr[i]))
        _set.add(arr[i])
    return solutions


arr = [8, 7, 2, 5, 3, 1]
sum = 10
print(pairWithGivenSum(arr, sum))

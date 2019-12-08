# Print all sub-arrays of an array having distinct elements
# not max
# for practice

def printAllSubArrays(a):
    n = len(a)
    _set = set()
    left = 0
    right = 0

    while right < n:
        while right < n and a[right] not in _set:
            _set.add(a[right])
            right += 1
        print(a[left:right])
        while right < n and a[right] in _set:
            _set.remove(a[left])
            left += 1


printAllSubArrays([5, 2, 3, 5, 4, 3])

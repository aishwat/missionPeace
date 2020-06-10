def findMin(a, l, r):
    # [10, 11, 12, 1, 2, 3]
    if len(a) == 1:
        return a[0]
    if len(a) == 0:
        return -1
    while l <= r:

        mid = l + r >> 1
        print(a[mid])
        if a[mid] < a[mid - 1] and a[mid] < a[mid + 1]:
            return mid
        elif a[mid] > a[mid + 1] and a[mid] > a[mid - 1]:
            return mid + 1
        elif a[mid] > a[r]:
            l = mid + 1
        else:
            r = mid - 1
    return mid


# a = [10, 11, 12, 1, 2, 3]
# a = [3, 4, 5, 1, 2]
# a = [1]
a = []
minIndex = findMin(a, 0, len(a) - 1)
print(minIndex)

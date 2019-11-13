def findMin(a, l, r):
    # [10, 11, 12, 1, 2, 3]
    while l <= r:
        mid = l + r >> 1
        if a[mid] < a[mid - 1] and a[mid] < a[mid] + 1:
            return mid
        elif a[mid] > a[mid + 1] and a[mid] > a[mid] + 1:
            return mid + 1
        elif a[mid] > a[r]:
            l = mid + 1
        else:
            r = mid - 1
    return mid


a = [10, 11, 12, 1, 2, 3]
minIndex = findMin(a, 0, len(a) - 1)
print(a[minIndex])

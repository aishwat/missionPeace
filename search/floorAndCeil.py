def floor(num, arr, l, r):
    floor = -1
    while l <= r:
        mid = l + r >> 1
        if arr[mid] == num:
            return arr[mid]
        elif num < arr[mid]:
            r = mid - 1
        else:
            floor = arr[mid]
            l = mid + 1
    return floor


def ceil(num, arr, l, r):
    ceil = -1
    while l <= r:
        mid = l + r >> 1
        if arr[mid] == num:
            return arr[mid]
        elif num < arr[mid]:
            ceil = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ceil


arr = [1, 4, 6, 8, 9]
for i in range(0, 11):
    print('i', i, 'floor', floor(i, arr, 0, len(arr) - 1), 'ceil', ceil(i, arr, 0, len(arr) - 1))

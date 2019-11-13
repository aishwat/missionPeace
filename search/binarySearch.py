def binary_search(key, arr, l, r):
    while l <= r:
        mid = l + r >> 1
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return -1


res = binary_search(3, [1, 2, 3, 4, 5], 0, 4)
print(res)

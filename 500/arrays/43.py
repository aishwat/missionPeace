# Find Triplet with given sum in an array
# dumb approach is to consider i, j, k loop, O(n3)
# use hasing for last loop, and directly check is sum-(A[i]+A[j]) exists, makes this O(n2)

def tripletExists(a, k):
    n = len(a)
    _set = set(a)

    for i in range(n):
        for j in range(i + 1, n):
            val = k - a[i] - a[j]
            if val in _set:
                print('triplet at ', a[i], a[j], val)


tripletExists([2, 7, 4, 0, 9, 5, 1, 3], 6)
# can be more optimized , instead of running j i+1 to n, keep 2 lo and hi pointers, do while lo<hi

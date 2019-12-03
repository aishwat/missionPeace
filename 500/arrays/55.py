# Print all Triplets that forms Arithmetic Progression
# can be done from hashing, but simple traversal is wasy
# O(n2) still,
# vl only work for triplets, not bigger, hashing can extend
def getTriplets(a):
    n = len(a)
    # a[i] - a[k] = a[k] - a[j]
    # 2*a[k] = a[i] + a[j]
    for k in range(1, n - 1):
        i = k - 1
        j = k + 1
        while (i >= 0 and j < n):
            if 2 * a[k] == a[i] + a[j]:
                print(a[i], a[k], a[j])
                i -= 1
                j += 1
            elif a[i] + a[j] < 2 * a[k]:
                j += 1
            else:
                i -= 1


getTriplets([1, 3, 5, 6, 8, 9, 15])

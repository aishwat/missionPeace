# https://media.geeksforgeeks.org/wp-content/cdn-uploads/Merge-Sort-Tutorial.png
def merge(self, L, R):
    if len(L) > len(R):
        self.merge(R, L)

    tmp = [0] * (len(R) + len(L))
    i = 0
    l, r = 0, 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            tmp[i] = L[l]
            l += 1
        else:
            tmp[i] = R[r]
            r += 1
        i += 1
    while r < len(R):
        tmp[i] = R[r]
        r += 1
        i += 1
    while l < len(L):
        tmp[i] = L[l]
        l += 1
        i += 1
    return (tmp)


def merge_sort(self, a):
    l = 0
    r = len(a)
    if len(a) > 1:
        m = l + r >> 1
        L = self.merge_sort(a[0:m])
        R = self.merge_sort(a[m:])
        a = self.merge(L, R)
        print(L, R)
    return a

#
# def merge_sort(a):
#     if len(a) > 1:
#         mid = len(a) // 2
#         L = a[0:mid]
#         R = a[mid:]
#         merge_sort(L)
#         merge_sort(R)
#         merge(a, L, R)
#
#
# def merge(a, L, R):
#     i = j = k = 0
#     while i < len(L) and j < len(R):
#         if L[i] < R[j]:
#             a[k] = L[i]
#             i += 1
#         else:
#             a[k] = R[j]
#             j += 1
#         k += 1
#     while i < len(L):
#         a[k] = L[i]
#         i += 1
#         k += 1
#     while j < len(R):
#         a[k] = R[j]
#         j += 1
#         k += 1


a = [38, 27, 43, 3, 9, 82, 10]
merge_sort(a)
print(a)

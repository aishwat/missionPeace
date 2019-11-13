# https://media.geeksforgeeks.org/wp-content/cdn-uploads/Merge-Sort-Tutorial.png
# def merge_sort(a, l, r):
#     if l < r:
#         m = l + r >> 1
#         merge_sort(a, l, m)
#         merge_sort(a, m + 1, r)
#         merge(a, l, m, r)
#
#
# def merge(a, l, m, r):
#     print('l', a[l], 'm', a[m], 'r', a[r])
#     i = j = 0
#     k = l
#     L = a[l: m + 1]
#     R = a[m + 1: r + 1]
#     print(L)
#     print(R)
#     print("")
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

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(a, L, R)


def merge(a, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1


a = [38, 27, 43, 3, 9, 82, 10]
merge_sort(a)
print(a)

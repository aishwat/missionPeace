def heapify(a, i, n):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[max] < a[l]:
        max = l
    if r < n and a[max] < a[r]:
        max = r
    if max != i:
        a[max], a[i] = a[i], a[max]
        heapify(a, max, n)


def build_max_heap(a):
    for i in range(len(a) // 2, -1, -1):
        heapify(a, i, len(a))


def heap_sort(a):
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i)


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heap_sort(a)
print(a)

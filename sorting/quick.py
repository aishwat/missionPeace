def quick_sort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        print(l, r, a, pivot, a[pivot])

        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)


def quick_sort_iter(a, l, r):
    size = r - l + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = l
    top += 1
    stack[top] = r

    while top >= 0:
        r = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(a, l, r)

        if p - 1 > l:  # if element of left of partition, till l
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        if p + 1 < r:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = r


def partition(a, l, r):
    pivot = a[r]
    j = l - 1
    for i in range(l, r):
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[j + 1], a[r] = a[r], a[j + 1]
    return j + 1



a = [10, 80, 30, 90, 40, 50, 70]
quick_sort(a, 0, len(a) - 1)
# quick_sort_iter(a, 0, len(a) - 1)
print(a)

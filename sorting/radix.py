def get_element(a, i, exp):
    return (a[i] / exp) % 10


def count_sort(a, exp):
    c = [0] * (10)  # auxillary array
    b = [0] * (len(a))  # b will have 1st element 0 always, to keep indexing clean

    for i in range(0, len(a)):
        c[(a[i] // exp) % 10] += 1
    for i in range(1, 10):
        c[i] += c[i - 1]

    print(c)
    for i in range(len(a) - 1, -1, -1):
        b[c[(a[i] // exp) % 10] - 1] = a[i]
        c[(a[i] // exp) % 10] -= 1  # for duplicate elements
    return b


def radix_sort(a):
    b = count_sort(a, 1)
    c = count_sort(b, 10)
    print(print(c))


a = [11, 10, 8, 6, 3, 1]
radix_sort(a)

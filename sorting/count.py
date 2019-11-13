def sort(a):
    c = [0] * (max(a) + 1)  # auxillary array
    b = [0] * (len(a) + 1)  # b will have 1st element 0 always, to keep indexing clean

    for i in range(0, len(a)):
        c[a[i]] = c[a[i]] + 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    print(c)
    for i in range(0, len(a)):
        b[c[a[i]]] = a[i]
        c[a[i]] -= 1  # for duplicate elements
    return b


a = [10, 8, 6, 3, 1]
print(sort(a))


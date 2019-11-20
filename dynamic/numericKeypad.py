def getCount(n):
    a = [1 for i in range(10)]
    b = [1 for i in range(10)]

    for i in range(1, n):
        b[0] = a[0] + a[8]
        b[1] = a[1] + a[2] + a[4]
        b[2] = a[2] + a[1] + a[3] + a[5]
        b[3] = a[3] + a[2] + a[6]
        b[4] = a[4] + a[1] + a[7] + a[5]
        b[5] = a[5] + a[2] + a[4] + a[6] + a[8]
        b[6] = a[6] + a[3] + a[5] + a[9]
        b[7] = a[7] + a[4] + a[8]
        b[8] = a[8] + a[5] + a[7] + a[9] + a[0]
        b[9] = a[9] + a[6] + a[8]

        _sum = 0
        for i in range(10):
            _sum += b[i]
        for i in range(10):
            a[i] = b[i]
    return _sum


print(getCount(5))

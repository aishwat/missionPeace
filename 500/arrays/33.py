def getMaxSumPath(x, y):
    common = list(set(x).intersection(set(y)))
    print(common)
    last_x = 0
    last_y = 0

    _sum = 0
    for i in range(len(common)):
        xSet = x[last_x:x.index(common[i])]
        ySet = y[last_y:y.index(common[i])]
        last_x = x.index(common[i]) + 1
        last_y = y.index(common[i]) + 1
        print(xSet, " ", ySet)

        _sum += max(sum(xSet), sum(ySet))

    xSet = x[last_x:]
    ySet = y[last_y:]
    print(xSet, " ", ySet)
    _sum += max(sum(xSet), sum(ySet))

    return _sum+sum(common)


x = [3, 6, 7, 8, 10, 12, 15, 18, 100]
y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
print(getMaxSumPath(x, y))

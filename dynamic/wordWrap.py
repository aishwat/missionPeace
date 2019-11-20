def getMinWrapCost(a, l):
    n = len(a)
    T = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        T[i][i] = (l - a[i]) * (l - a[i])
    for i in range(n - 1):
        T[i][i + 1] = (l - a[i] - a[i + 1] - 1) * (l - a[i] - a[i + 1] - 1)
    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l;
            T[i][j] = 99;
            for k in range(i, j):
                T[i][j] = min(T[i][j], T[i][k] + T[k + 1][j])
    for i in range(n):
        print(T[i][:])


MAX = 999;


def getMinWrap(a, l):
    n = len(a)
    T = [[MAX for i in range(n)] for i in range(n)]
    for i in range(n):
        T[i][i] = (l - a[i]) * (l - a[i])
    for i in range(n - 1):
        T[i][i + 1] = (l - a[i] - a[i + 1] - 1) * (l - a[i] - a[i + 1] - 1)
    # skipping INF fills, works for this input

    minCost = [999] * len(a)
    pos = [0] * len(a)
    for i in range(len(a) - 1, -1, -1):
        minCost[i] = T[i][len(a) - 1]
        pos[i] = len(a)
        for j in range(len(a) - 1, i, -1):
            if T[i][j - 1] == MAX:
                continue;
            if minCost[i] > minCost[j] + T[i][j - 1]:
                minCost[i] = minCost[j] + T[i][j - 1]
                pos[i] = j

    print(minCost)
    print(pos)


a = [6, 3, 5, 2, 4]
# getMinWrapCost(a, 10)
getMinWrap(a, 10)

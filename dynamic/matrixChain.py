def getMinMulti(a):
    n = len(a)
    T = [[0 for i in range(n)] for i in range(n)]

    for l in range(2, len(a)):
        for i in range(0, len(a) - l):
            j = i + l;
            T[i][j] = 999;
            # print(i," ", j)
            for k in range(i + 1, j):
                # print(i, " ", k, " ", j)
                q = T[i][k] + T[k][j] + (a[i] * a[k] * a[j])
                T[i][j] = min(q, T[i][j])

    for i in range(len(T)):
        print(T[i][:])


p = [1, 2, 3, 4]
getMinMulti(p)

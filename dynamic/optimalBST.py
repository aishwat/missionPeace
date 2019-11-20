def getOptimalBST(keys, freq):
    n = len(keys)
    T = [[999 for i in range(n)] for i in range(n)]

    for i in range(n):
        T[i][i] = freq[i]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l

            _sum = sum(freq[i:j+1])
            for k in range(i, j+1):  # both inclusive
                # print(i, " ", k, " ", j, " - ", _sum)
                if k == i:
                    tmp = T[k + 1][j]
                elif k == j:
                    tmp = T[i][k - 1]
                else:
                    tmp = T[i][k - 1] + T[k + 1][j]
                # print(_sum+tmp)
                T[i][j] = min(T[i][j], _sum + tmp)

    for i in range(n):
        print(T[i][:])


keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]
getOptimalBST(keys, freq)

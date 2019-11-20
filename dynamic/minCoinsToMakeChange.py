def getMinCount(coins, V):
    V = V+1
    T = [[0 for i in range(V)] for i in range(len(coins))]

    T[:][0] = 1
    for i in range(1, V):
        T[0][i] = i

    for i in range(1, len(coins)):
        for j in range(1, V):
            T[i][j] = min(T[i - 1][j], 1 + T[i][j - coins[i]])

    return T


a = getMinCount([1, 5, 6, 9], 11)
for i in range(len(a)):
    print(a[i][:])

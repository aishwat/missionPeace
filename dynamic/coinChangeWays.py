def getNWays(n, coins):
    rows = len(coins)
    cols = n + 1

    L = [[0 for i in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                L[i][j] = 1

            elif coins[i] > j:
                L[i][j] = L[i - 1][j]

            else:
                L[i][j] = L[i - 1][j] + L[i][j - coins[i]]
    for i in range(rows):
        print(L[i][:])

coins = [1, 2, 3]
n = 4
getNWays(4, coins)

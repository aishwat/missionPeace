def getMaxProfits(prices, k):
    T = [[0 for i in range(len(prices))] for i in range(k)]

    # T[0][:] = 0
    # T[:][0] = 0

    for i in range(1, k):
        for j in range(1, len(prices)):
            no_trx = T[i][j - 1]
            yes_trx = -99
            for m in range(0, j):
                yes_trx = max(yes_trx, prices[j] - prices[m] + T[i - 1][m])
            T[i][j] = max(no_trx, yes_trx)
    for i in range(k):
        print(T[i][:])


prices = [2, 5, 7, 1, 4, 3, 1, 3]
k = 3
getMaxProfits(prices, k+1)

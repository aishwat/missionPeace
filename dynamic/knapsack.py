def getMaxVal(val, wt, W):
    T = [[0 for i in range(W + 1)] for i in range(len(wt))]

    for i in range(len(wt)):
        for j in range(W + 1):
            # print(i, " ", j, " ", T[i-1][j])
            if wt[i] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], val[i] + T[i - 1][j - wt[i]])

    # print(T[len(wt)-1][W-1])
    for i in range(len(T)):
        print(T[i][:])


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
getMaxVal(val, wt, W)

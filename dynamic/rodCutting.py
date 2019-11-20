def getMaxProfit(a):
    T = [[0 for i in range(len(a) + 1)] for i in range(len(a))]

    for i in range(0, len(a)):
        for j in range(0, len(a) + 1):
            if i == 0:
                T[i][j] = a[0] * j  # given a[0] = 1 #actually for len 1
                # so rod len = i+1
            elif j == 0:
                T[i][j] = 0
            elif j < i + 1:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], a[i] + T[i][j - (i + 1)])
    for i in range(len(T)):
        print(T[i][:])


a = [1, 5, 8, 9, 10, 17, 17, 20]
getMaxProfit(a)

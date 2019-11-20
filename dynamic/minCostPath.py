def minCostPath(cost):
    rows = len(cost)
    cols = len(cost[0])
    T = [row[:] for row in cost]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                T[0][0] = cost[0][0]
            elif i == 0 and j > 0:
                T[i][j] = T[i][j - 1] + cost[i][j]
            elif j == 0 and i > 0:
                T[i][j] = T[i - 1][j] + cost[i][j]
            else:
                T[i][j] = min(T[i - 1][j], T[i - 1][j - 1], T[i][j - 1]) + cost[i][j]

    for row in range(len(T)):
        print(T[row][:])


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

minCostPath(cost)

INF = 999


def minCost(cost, N):
    T = [0] * N
    T[N - 1] = 0  # cost to reach dest from dest is 0
    for i in range(N - 1, -1, -1):
        T[i] = cost[i][N - 1]

        for j in range(i + 1, N):
            if cost[i][j] != INF:
                T[i] = min(T[i], cost[i][j] + T[j])
    return T


cost = [[0, 15, 80, 90],
        [INF, 0, 40, 50],
        [INF, INF, 0, 70],
        [INF, INF, INF, 0]]

print("The Minimum cost to reach station is ", minCost(cost, 4))

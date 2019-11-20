def countWays(n, m):
    n += 1

    # now indexes starting from 1
    T = [0 for i in range(n)]
    for i in range(1, m + 1):
        T[i] = i

    for i in range(m + 1, n):
        for j in range(i - m, i):
            T[i] += T[j]

    return T


print(countWays(4, 2))

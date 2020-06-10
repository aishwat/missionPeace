def getMinPartitions(a):
    T = [[0 for i in range(len(a))] for i in range(len(a))]

    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            T[i][i + 1] = 0
        else:
            T[i][i + 1] = 1

    for l in range(2, len(a)):
        for i in range(0, len(a) - l):
            j = i + l
            if (a[i] == a[j]):
                T[i][j] = T[i + 1][j - 1]
            else:
                T[i][j] = min(T[i + 1][j], T[i][j - 1]) + 1

    for i in range(len(T)):
        print(T[i][:])

    for l in range(2, len(a)):
        for i in range(0, len(a) - l):
            j = i + l
            if (a[i] == a[j]):
                T[i][j] = T[i + 1][j - 1]
            else:
                T[i][j] = 99
                for k in range(i, j):  # i inclusive, j exclusive
                    T[i][j] = min(T[i][j], 1 + T[i][k] + T[k + 1][j])
    print()
    for i in range(len(T)):
        print(T[i][:])

str = "ababa";

print(getMinPartitions(str))

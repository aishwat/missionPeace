def getMax(A):
    N = len(A) + 2  # added boundaries
    A = [1] + A + [1]  # Add Bordering Balloons
    T = [[0 for x in range(N + 2)] for y in range(N + 2)]  # Declare DP Array

    for l in range(2, N):
        for i in range(0, N - l):
            j = i + l
            for k in range(i + 1, j):
                T[i][j] = max(T[i][j], T[i][k] + A[i] * A[k] * A[j] + T[k][j])

    for i in range(N + 2):
        for j in range(N + 2):
            print(T[i][j], end=" ")
        print("")
    print(T[0][N - 1])


A = [3, 1, 5, 8]
getMax(A)

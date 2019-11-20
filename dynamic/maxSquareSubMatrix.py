def getMaxSquare(M):
    rows = len(M)
    cols = len(M[0])
    T = [[M[i][j] for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if M[i][j] == 1:
                T[i][j] = min(T[i - 1][j], T[i - 1][j - 1], T[i][j - 1]) + 1
            else:
                T[i][j] = 0
    for i in range(rows):
        print(T[i][:])


M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

getMaxSquare(M)

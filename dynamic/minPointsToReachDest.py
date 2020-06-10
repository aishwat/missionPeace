def getMinPointsToReachDest(points):
    rows = len(points)
    cols = len(points[0])
    T = [[0 for i in range(cols)] for i in range(rows)]

    if points[rows - 1][cols - 1] <= 0:
        T[rows - 1][cols - 1] = - points[rows - 1][cols - 1] + 1
    else:
        T[rows - 1][cols - 1] = 1

    # last column
    for i in range(rows - 2, -1, -1):
        T[i][cols - 1] = T[i + 1][cols - 1] - points[i][cols - 1]
        if T[i][cols - 1] <= 0:
            T[i][cols - 1] = 1

    # last column
    for j in range(cols - 2, -1, -1):
        T[rows - 1][j] = T[rows - 1][j + 1] - points[rows - 1][j]
        if T[rows - 1][j] <= 0:
            T[rows - 1][j] = 1

    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            min_points_needed = min(T[i + 1][j], T[i][j + 1])
            T[i][j] = min_points_needed - points[i][j]
            if (T[i][j] <= 0):
                T[i][j] = 1

    for i in range(rows):
        print(T[i][:])


# points = [[-2, -3, 3],
#           [-5, -10, 1],
#           [10, 30, -5]]
points = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, -10]]
getMinPointsToReachDest(points)
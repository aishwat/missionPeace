MIN = -999


def getMaxPoints(a, mem, x, y1, y2):
    # print(x, " ", y1, " ", y2)
    rows = len(a)
    cols = len(a[0])
    # base
    # if x >= rows or x < 0 or y1 >= cols or y1 < 0 or y2 >= cols or y2 < 0:
    if (x >= 0 and x < rows and y1 >= 0
        and y1 < cols and y2 >= 0 and y2 < cols) == False:
        return MIN
    # end case
    if x == rows - 1 and y1 == 0 and y2 == cols - 1:
        # print("at last ")
        mem[x][y1][y2] = a[x][y1] + a[x][y2]
        return a[x][y1] + a[x][y2]

    if x == rows - 1:
        # print("at last row")
        return MIN

    if mem[x][y1][y2] != MIN:
        return mem[x][y1][y2]

    if y1 == y2:
        temp = a[x][y1]
    else:
        temp = a[x][y1] + a[x][y2]

    ans = 0
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 - 1, y2 - 1))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 - 1, y2))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 - 1, y2 + 1))

    ans = max(ans, getMaxPoints(a, mem, x + 1, y1, y2 - 1))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1, y2))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1, y2 + 1))

    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 + 1, y2 - 1))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 + 1, y2))
    ans = max(ans, getMaxPoints(a, mem, x + 1, y1 + 1, y2 + 1))

    mem[x][y1][y2] = ans + temp
    return mem[x][y1][y2]


arr = [[3, 6, 8, 2],
       [5, 2, 4, 3],
       [1, 1, 20, 10],
       [1, 1, 20, 10],
       [1, 1, 20, 10],
       ]
rows = len(arr)
cols = len(arr[0])
mem = [[[MIN for i in range(cols)] for i in range(cols)] for i in range(rows)]

print(getMaxPoints(arr, mem, 0, 0, cols - 1))

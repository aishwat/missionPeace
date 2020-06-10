import math
# https://ide.geeksforgeeks.org/LhGXEan4jR

def getMinSquares(n):
    # T = [0] * n+1
    T = [0, 1, 2, 3]

    for i in range(4, n + 1):
        # T[i] = i
        T.append(i)
        for j in range(1, math.ceil(math.sqrt(i)) + 1):
            temp = j * j

            if temp < i:
                # use temp as one factor
                T[i] = min(T[i], 1 + T[i - temp])

    print(T)


getMinSquares(41)

# Find equilibrium index of an array

def getIndexes(a):
    L = [0] * len(a)
    for i in range(1, len(a)):
        L[i] = L[i - 1] + a[i]

    R = [0] * len(a)
    for i in range(len(a) - 2, -1, -1):
        R[i] = R[i + 1] + a[i]
    print('a', a)
    print('L', L)
    print('R', R)

    for i in range(len(a)):
        if L[i] == R[i]:
            print(i, end=" ")


a = [0, -3, 5, -4, -2, 3, 1, 0]
getIndexes(a)

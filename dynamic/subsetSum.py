def isSubsetSum(a, sum):
    T = [[False for i in range(sum + 1)] for i in range(len(a))]

    T[0][a[0]] = True
    T[:][0] = True

    for i in range(1, len(a)):
        for j in range(1, sum+1):
            if j < a[i]:
                T[i][j] = T[i - 1]
            else:
                T[i][j] = T[i - 1] or T[i - 1][j - a[i]]

    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j]:
                print('T', end=" ")
            else:
                print('F', end=" ")
        print(" ")
    # print(T)

a = [2, 3, 7, 8, 10]
isSubsetSum(a, 11)

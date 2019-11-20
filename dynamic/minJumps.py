def getMinJumps(a):
    T = [i for i in range(len(a))]
    T[0] = 0
    print(T)
    for i in range(1, len(a)):
        for j in range(i):
            if j + a[j] >= i and T[i] > T[j] + 1:
                T[i] = T[j] + 1

    print(T)


getMinJumps([1, 3, 5, 8, 9, 2])

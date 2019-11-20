def maxSumIncreasingSubseq(a):
    T = [a[i] for i in range(len(a))]

    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j] and T[i] < a[i] + T[j]:
                T[i] = a[i] + T[j]

    print(T)


arr = [1, 101, 2, 3, 100, 4, 5]
maxSumIncreasingSubseq(arr)

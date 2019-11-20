def lcs(A, B):
    row = len(A)
    col = len(B)
    LCS = [[0 for i in range(col + 1)] for i in range(row + 1)]
    # print(LCS)

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if A[i-1] == B[j-1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    for i in range(row):
        print(LCS[i][:])

A = ['a', 'b', 'c', 'd']
B = ['b', 'c']
lcs(A, B)

def editDistance(str1, str2):
    row = len(str1)
    print(row)
    col = len(str2)
    print(col)
    T = [[0 for i in range(col + 1)] for i in range(row + 1)]
    # for row in range(row):
    #     print(T[row][:])

    for i in range(0, row + 1):
        for j in range(0, col + 1):
            if i == 0:
                T[i][j] = j
            elif j == 0:
                T[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i - 1][j - 1], T[i][j - 1])

    for row in range(row+1):
        print(T[row][:])


str1 = "sunday"
str2 = "saturday"
# print(str1)

editDistance(str1, str2)

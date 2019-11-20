def getLongestPalindromicSub(str):
    n = len(str)
    T = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        T[i][i] = True
    maxL = 0
    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l;

            if str[i] == str[j] and T[i + 1][j - 1]:
                T[i][j] = True
            
                maxL = l+1
            else:
                T[i][j] = False
    print(maxL)
    for i in range(n):
        print(T[i][:])


str = "geekeg"
getLongestPalindromicSub(str)

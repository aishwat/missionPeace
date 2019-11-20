def getLCPSubseq(str):
    T = [[0 for i in range(len(str) + 1)] for i in range(len(str) + 1)]

    for i in range(len(str)):
        T[i][i] = 1

    for l in range(2, len(str) + 1):
        for i in range(0, len(str) - l + 1):
            j = i + l - 1;
            print(str[i], " ", str[j])
            if str[i] == str[j] and l == 2:
                T[i][j] = 2
            elif str[i] == str[j]:
                T[i][j] = T[i + 1][j - 1] + 2
            else:
                T[i][j] = max(T[i + 1][j], T[i][j - 1])
    for i in range(len(T)):
        print(T[i][:])


getLCPSubseq("agbdba")

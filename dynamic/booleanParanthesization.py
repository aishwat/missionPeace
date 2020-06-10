def countParenth(symbols, operators):
    n = len(symbols)
    T = [[0 for i in range(n)] for i in range(n)]  # no of ways we can make expr T
    F = [[0 for i in range(n)] for i in range(n)]  # no of ways we can make expr F

    for i in range(n):
        if symbols[i] == 'T':
            T[i][i] = 1
            F[i][i] = 0
        else:
            T[i][i] = 0
            F[i][i] = 1

    for l in range(1, n):
        # print("====",l,"=====")
        for i in range(0, n - l):
            j = i + l
            # print("i",i, "j",j)
            for k in range(i, j):
                # print(k, operators[k])
                t_ik = T[i][k] + F[i][k]
                t_kj = T[k + 1][j] + F[k + 1][j]
                if operators[k] == '&':
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += (t_ik * t_kj) - T[i][k] * T[k + 1][j]
                if operators[k] == '|':
                    T[i][j] += (t_ik * t_kj) - F[i][k] * F[k + 1][j]
                    F[i][j] += F[i][k] * F[k + 1][j]
                if operators[k] == '^':
                    T[i][j] += T[i][k] * F[k + 1][j] + F[i][k] * T[k + 1][j]
                    F[i][j] += T[i][k] * T[k + 1][j] + F[i][k] * F[k + 1][j]

    for i in range(n):
        print(T[i][:])
    print()
    for i in range(n):
        print(F[i][:])


symbols = "TTFT"
operators = "|&^"

print(countParenth(symbols, operators))

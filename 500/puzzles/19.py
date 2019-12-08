# Perform Division of two numbers without using division operator (/)
def divide(N, D):

    print(N)
    print(D)
    for i in range(len(str(N))):
        t = N - D
        Q = 0
        print(t)
        if t >= 0:
            Q = Q | 1
            N = t
        Q << 1
        N << 1
    print(Q, N)


divide(1001, 0011)


# For instance if N=9 and D=3, then we have N=1001, D=11.
# So the first thing to do is to left shift D by 2 so that the leading one matches that of N,
# i.e. you work with D=1100

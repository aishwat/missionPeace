def getLIS(a):
    T = [1 for i in range(len(a))]
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j] and T[i] < T[j] + 1:
                T[i] = T[j] + 1
    return T


def getLDS(a):
    T = [1 for i in range(len(a))]
    for i in range(len(a) - 2, -1, -1):
        for j in range(len(a) - 1, i, -1):
            if a[i] > a[j] and T[i] < T[j] + 1:
                T[i] = T[j] + 1
    # for i in reversed(range(len(a) - 1)):  # loop from n-2 downto 0
    #     for j in reversed(range(i - 1, len(a))):  # loop from n-1 downto i-1
    #         if (a[i] > a[j] and T[i] < T[j] + 1):
    #             T[i] = T[j] + 1
    return T


a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
     3, 11, 7, 15]

lis = (getLIS(a))
lds = (getLDS(a))
print(lis)
print(lds)

max_ = lis[0] + lds[0] - 1
for i in range(len(a)):
    max_ = max(max_, lis[i] + lds[i] - 1)

print(max_)

import math


def getPowerSet(s):
    n = int(math.pow(2, len(s)))

    for i in range(n):
        # we know this i is a len(s) bits number, print its set bits
        # use j for pos
        for j in range(len(s)):
            # if i & (1 << j):
            #     print('1', end='')
            # else:
            #     print('0', end='')
            if i & (1 << j):
                print(s[j], end='')
        print()


getPowerSet([1, 2, 3])

def findNdigitNumsUtil(n, sum, out, index):
    if index > n or sum < 0:
        return ""
    if index == n and sum == 0:
        # print
        for i in range(len(out)):
            print(out[i], end='')
        print()
        return
    if index == n and sum != 0:
        # do nothing
        return

    for i in range(10):
        out[index] = i
        findNdigitNumsUtil(n, sum - i, out, index + 1)


def findNdigitNums(n, sum):
    out = [False] * n
    for i in range(1, 10):
        out[0] = i
        findNdigitNumsUtil(n, sum - i, out, 1)


findNdigitNums(2, 3)

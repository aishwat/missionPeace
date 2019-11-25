# Find index of 0 to replaced to get maximum length sequence of continuous ones
# 2 solutions, 1st is very tricky, need to maintain left pointer and coumnt
# 2nd one here, kinda hack

def getIndex(a):
    n = len(a)
    for i in range(1, n):
        if a[i] == 1:
            a[i] += a[i - 1]
    print(a)

    i = n - 1
    while i >= 0:
        if a[i] != 0:
            count = a[i]
            # print(a[i - count + 1:i + 1])  # to include i , do i+1
            a[i - count + 1:i + 1] = [count] * (count)
            i = i - count
        else:
            i -= 1
    print(a)

    _max = -99
    for i in range(1, n - 1):
        if a[i] == 0 and a[i - 1] + a[i + 1] > _max:
            _max = a[i - 1] + a[i + 1]
            index = i

    print(index)


a = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
getIndex(a)

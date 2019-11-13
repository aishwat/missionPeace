def get_closest_pair(a, b, sum):
    diff = 999
    l, r = 0, len(b) - 1
    res = ()
    while l < len(a) and r > 0:
        temp = abs(a[l] + b[r] - sum)
        if temp < diff:
            diff = temp
            res = (l, r)
        elif (a[l] + b[r]) > sum:
            r -= 1
        else:
            l += 1
    return res


A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8]
C = 9
l, r = get_closest_pair(A, B, C)
print(A[l], B[r])

A = [5, 10, 20]
B = [1, 2, 30]
C = 13
l, r = get_closest_pair(A, B, C)
print(A[l], B[r])

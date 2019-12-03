# tricky
# Rearrange array such that A[A[i]] is set to i for every element A[i]
# https://drive.google.com/open?id=16M4C5AwmuK7FGM84Bx_ql7DDdRTscFC-
def rearrange(a):
    n = len(a)
    for i in range(n):
        a[a[i]%n] += n * i
    for i in range(n):
        a[i] //= n

    print(a)


rearrange([1, 3, 4, 2, 0])

# [4, 0, 3, 1, 2]

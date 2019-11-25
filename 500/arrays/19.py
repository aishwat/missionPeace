# Replace each element of array with product of every other element without using / operator

def getProduct(a):
    n = len(a)

    left = [a[0]] * n
    for i in range(1, n):
        left[i] = left[i - 1] * a[i]

    right = [a[n - 1]] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * a[i]

    print(left)
    print(right)

    pr = [0] * n
    for i in range(n):
        if i == 0:
            pr[i] = right[1]
        elif i == n - 1:
            pr[i] = left[n - 2]
        else:
            pr[i] = left[i - 1] * right[i + 1]

    print(pr)


getProduct([1, 2, 3, 4, 5])

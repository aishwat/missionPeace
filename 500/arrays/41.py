# Decode the array constructed from another array
# good problem

# m = n(n-1)/2 or n2 – n – 2m = 0
# Solving above equation, we get
# n = (sqrt(8m+1) + 1)/2
# b^2 - 4ac rule

# https://drive.google.com/open?id=16Go1Jdvb496H8RDZWzgnvlyCuGTztDoV

import math


def get_original_arr(a):
    m = len(a)
    n = int((math.sqrt(8 * m + 1) + 1) // 2)
    print(n)

    A = [0] * n
    A[0] = (a[0] + a[1] - a[n - 1]) // 2

    for i in range(1, n):
        A[i] = a[i - 1] - A[0]
    print(A)


get_original_arr([3, 4, 5, 5, 6, 7])

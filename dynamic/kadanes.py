def largestSumContiguous(a):
    max_so_far = max_ending_here = 0
    for i in range(0, len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largestSumContiguous(a))

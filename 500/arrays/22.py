# simple kadane's, just for practice
def getMaxSubArray(a):
    max_so_far = -1
    max_ending_here = 0

    for i in range(len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(getMaxSubArray(a))

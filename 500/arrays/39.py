# Find maximum sum of subsequence with no adjacent elements
# good simple problem,
# either consider current element and go back two step or
# dont consider current element and consider sum till one step back

# either include current element or not
def getMaxNonAdjSum(A):
    n = len(A)
    maxSum = [A[i] for i in range(n)]

    for i in range(2, n):
        maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + A[i])

    print(maxSum)


A = [1, 2, 9, 4, 5, 0, 4, 11, 6]
getMaxNonAdjSum(A)

# [1, 2, 10, 10, 15, 15, 19, 26, 26]
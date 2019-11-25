# Find maximum difference between two elements in the array by satisfying given constraints
# variant of buy sell stock at most 1 trx
# naive - O(n2), this O(n)
# right to left traversal and maintain max and maxdiff
def getMaxDiff(a):
    maxDiff = -1
    maxTillNow = len(a) - 1
    minTillNow = -1

    for i in range(len(a) - 1, -1, -1):
        if a[maxTillNow] > a[i] and a[maxTillNow] - a[i] > maxDiff:
            maxDiff = a[maxTillNow] - a[i]
            minTillNow = i
        if a[maxTillNow] < a[i]:
            maxTillNow = i
    print(maxDiff, " ", minTillNow, " ", maxTillNow)


a = [2, 7, 9, 5, 1, 3, 5]
getMaxDiff(a)

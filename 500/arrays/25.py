# Find all distinct combinations of given length

def getCombinationsUtil(startIndex, out, a, k):

    if k == 0:
        print(out)
        # out = out[:-1]
        return
    for i in range(startIndex, len(a)):
        # print(' appending', a[i])
        # out = str(out) + str(a[i]) #important, doesnt work this way
        getCombinationsUtil(i + 1, str(out) + str(a[i]), a, k - 1)


def getCombinations(a, k):
    n = len(a)
    for i in range(len(a)):
        out = str(a[i])
        # print('appending', a[i])
        getCombinationsUtil(i + 1, out, a, k - 1)


a = [1, 2, 3, 4]
k = 2
getCombinations(a, k)

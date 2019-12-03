# Print all distinct Subsets of a given Set

def getSubsets(originalSet):
    subsets = []
    n = 2 * (len(originalSet))
    for i in range(n):
        subset = []
        for j in range(len(originalSet)):
            if (i & 1 << j):
                subset.append(originalSet[j])
        subsets.append(subset)
    return subsets



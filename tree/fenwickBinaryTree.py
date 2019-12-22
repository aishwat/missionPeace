def createTree(arr):
    print(arr)
    tree = [0] * len(arr)
    # 0th node is blank
    for i in range(1, len(arr) + 1):
        updateTree(tree, i, arr[i - 1])
    return tree


def updateTree(tree, index, val):
    while index < len(tree):
        tree[index] += val
        index = getNext(index)


def getParent(index):
    return index - (index & -index)


def getNext(index):
    return index + (index & -index)


def getSum(tree, index):
    index += 1
    sum = 0
    while index > 0:
        sum += tree[index]
        index = getParent(index)
    return sum


arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
_tree = createTree(arr)
print(_tree)  # [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9]
print(getSum(_tree, 4))  # 3,2,-1, 6, 5 = 15

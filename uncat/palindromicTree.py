class Node:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.length = -1
        self.insertEdg = {'a': None, 'b': None, 'c': None}
        self.suffixEdg = -1


currNode = 3
ptr = -1


def insert(s, tree, idx):
    global currNode, ptr

    # CASE 1:getting X and insert edge
    #
    tmp = currNode
    while True:
        currLen = tree[tmp].length
        if idx - currLen - 1 >= 0 and s[idx] == s[idx - currLen - 1]:
            # Found X such that s[idx] X s[idx]
            break
        tmp = tree[tmp].suffixEdg

    if tree[tmp].insertEdg[s[idx]] != None:
        currNode = tree[tmp].insertEdg[s[idx]]
        return

    ptr += 1
    tree[tmp].insertEdg[s[idx]] = ptr
    tree[ptr].length = tree[tmp].length + 2  # can be 1
    tree[ptr].end = idx
    tree[ptr].start = idx - tree[ptr].length + 1
    currNode = ptr

    print(s[idx])

    # CASE 2: getting Y and setting suffix Edge
    #
    tmp = tree[tmp].suffixEdg
    print(tmp)
    # special case, if tree[ptr].length == 1
    # otherwise tmp is pointing to root1, and it's suffix is itself, so gets stuck in loop
    if tree[currNode].length == 1:
        tree[currNode].suffixEdg = 2
        return

    while True:
        currLen = tree[tmp].length
        if idx - currLen - 1 >= 0 and s[idx] == s[idx - currLen - 1]:
            # Found Y such that s[idx] Y s[idx]
            break
        tmp = tree[tmp].suffixEdg

    tree[currNode].suffixEdg = tree[tmp].insertEdg[s[idx]]
    print("setting suffix edge", tree[currNode].suffixEdg)


def main():
    global ptr, currNode
    root1 = Node()
    root1.length = -1
    root1.suffixEdg = 1

    root2 = Node()
    root2.length = 0
    root2.suffixEdg = 1

    tree = [None, root1, root2]
    ptr = 2
    currNode = 1

    s = "abcbab"

    for i in range(len(s)):
        tree.append(Node())

    for i in range(len(s)):
        insert(s, tree, i)
    print("-------------")
    print(ptr)

    for i in range(3, ptr + 1):
        print(i, ")", end=" ")
        for j in range(tree[i].start, tree[i].end + 1):
            print(s[j], end=" ")
        print()


main()



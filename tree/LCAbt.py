class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


import queue


# for bst, just find root such that e1<root<e2
def getLCA(root, e1, e2):
    if root.key == e1:
        print("got ", e1)
        return root
    if root.key == e2:
        print("got ", e2)
        return root

    L = R = None
    if root.left:
        L = getLCA(root.left, e1, e2)
    if root.right:
        R = getLCA(root.right, e1, e2)

    if L and R:
        return root
    else:
        return L or R


n9 = Node(9)
n5 = Node(5)
n11 = Node(11, n5, n9)

n2 = Node(2)
n6 = Node(6, n2, n11)

n7 = Node(7)
n13 = Node(13, n7)
n8 = Node(8, None, n13)

r = Node(3, n6, n8)

print(getLCA(r, 2, 5))

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def isBST(root, _min, _max):
    if not root:
        return True
    if root.key < _min or root.key > _max:
        return False

    return isBST(root.left, _min, root.key) and isBST(root.right, root.key, _max)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
print(isBST(root, -999, 999))
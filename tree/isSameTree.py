class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def isSameTree(root1, root2):
    if root1.left and root2.left:
        return root1.left.key == root2.left.key and isSameTree(root1.left, root2.left)
    if root1.right and root2.right:
        return root1.right.key == root2.right.key and isSameTree(root1.right, root2.right)
    if root1.key == root2.key:
        return True

    return False


root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
print(isSameTree(root1, root2))

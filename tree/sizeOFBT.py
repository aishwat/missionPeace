class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


def height(root):
    if not root:
        return 0
    lh = 1 + height(root.left)
    rh = 1 + height(root.right)
    return max(lh, rh)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(size(root))
print(height(root))

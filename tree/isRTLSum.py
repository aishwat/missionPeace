class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def isRTLSum(root, sum):
    if not root:
        return False
    if root.left == None and root.right == None and sum == root.key:
        return True
    sum = sum - root.key
    # print(sum)
    l = isRTLSum(root.left, sum)
    r = isRTLSum(root.right, sum)
    return l or r


s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
print(isRTLSum(root, s))

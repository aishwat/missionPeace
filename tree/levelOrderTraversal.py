class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


import queue


def levelOrderTraversal(root):
    q = queue.Queue(maxsize=10)
    q.put(root)

    while not q.empty():
        root = q.get()
        print(root.key, end=" ")
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
levelOrderTraversal(root)

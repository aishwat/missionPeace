import queue


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def postorder(root):
    # only traversal which needs 2 stacks
    s1 = queue.LifoQueue(maxsize=15)  # LifoQueue is stack
    s2 = queue.LifoQueue(maxsize=15)
    s1.put(root)

    while not s1.empty():
        root = s1.get()
        s2.put(root)

        if root.left:
            s1.put(root.left)
        if root.right:
            s1.put(root.right)

    while not s2.empty():
        root = s2.get()
        print(root.key, end=" ")


def preorder(root):
    # first right then left
    s = queue.LifoQueue(maxsize=15)
    s.put(root)

    while not s.empty():
        root = s.get()
        print(root.key, end=" ")

        if root.right:
            s.put(root.right)

        if root.left:
            s.put(root.left)


def inorder(root):
    # LVR
    s = queue.LifoQueue(maxsize=15)

    while True:
        if s.empty() and not root:
            break;

        if root != None:
            s.put(root)
            root = root.left
        else:
            root = s.get()
            print(root.key, end=" ")
            root = root.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

postorder(root)
# #4 5 2 6 7 3 1
print("")
preorder(root)
# #1 2 4 5 3 6 7
print("")
inorder(root)
# #4 2 5 1 6 3 7

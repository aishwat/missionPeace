class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


import queue


def spiralTraversal(root):
    print("")
    s1 = queue.LifoQueue(maxsize=15)
    s2 = queue.LifoQueue(maxsize=15)
    s1.put(root)

    while True:
        while not s1.empty():
            root = s1.get()
            print(root.key, end=" ")
            if root.left:
                s2.put(root.left)
            if root.right:
                s2.put(root.right)
        print()

        while not s2.empty():
            # first right then left, s1 is opp
            root = s2.get()
            print(root.key, end=" ")
            if root.right:
                s1.put(root.right)
            if root.left:
                s1.put(root.left)
        print()
        if s1.empty() and s2.empty():
            return


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
spiralTraversal(root)

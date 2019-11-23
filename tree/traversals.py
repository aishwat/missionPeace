class Node:
    def __init__(self, key, l=None, r=None):
        self.key = key
        self.l = l
        self.r = r

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.l) + " " + str(self.r) + ")"


def preorder(root):
    if root != None:
        print(root.key, end=" ")
        preorder(root.l)
        preorder(root.r)


def inorder(root):
    if root != None:
        inorder(root.l)
        print(root.key, end=" ")
        inorder(root.r)


def postorder(root):
    if root != None:
        postorder(root.l)
        postorder(root.r)
        print(root.key, end=" ")


root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)

print("preorder")
preorder(root)

print("\ninorder")
inorder(root)

print("\npostorder")
postorder(root)

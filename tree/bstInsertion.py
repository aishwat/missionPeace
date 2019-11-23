class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def insert(root, node):
    data = node.key

    if node == None:
        return node

    rootOld = None
    while root:
        rootOld = root
        if data <= root.key:
            root = root.left
        else:
            root = root.right
    # at this point rootOld points to correct node

    # leaf
    if data < rootOld.key:
        rootOld.left = node
    else:
        rootOld.right = node
    return root


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


inorder(r)

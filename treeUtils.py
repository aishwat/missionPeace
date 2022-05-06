class TreeNode:
    def __str__(self):
        return str(self.val) or 'None'

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.sum = None
        self.next = None


class Tree:
    def __init__(self, a):
        if a:
            self.root = self.createTree(a, 0)

    def createTree(self, a, i):
        if i < len(a) and a[i] is not None:
            node = TreeNode(a[i])
            node.left = self.createTree(a, (2 * i) + 1)
            node.right = self.createTree(a, (2 * i) + 2)
            return node
        else:
            return  # TreeNode(None)

    @classmethod
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        # print(root.val, (root.next and root.next.val))
        self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
        if root and root.left:
            self.preorder(root.left)
        if root and root.right:
            self.preorder(root.right)

# a = [0, 1, 2, 3, 4, 5, 6]
# a = [3, 9, 20, None, None, 15, 7]
#
# Tree = Tree()
# root = Tree.createTree(a, 0)
# Tree.preorder(root)

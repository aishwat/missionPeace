class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        # print(root, key)
        if root == None:
            return TreeNode(key)
        elif root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)  # >1 means leftH > rightH, so it was a left inserted

        # LL
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        # RR
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # LR,
        # 1. L so still leftH > rightH so balance >1
        # 2. R so key ,must be greater than root's left
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, x):
        # print(x)
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        # print(y)
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, node):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def preOrder(self, root):

        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


myTree = AVLTree()
_root = None

_root = myTree.insert(_root, 10)
_root = myTree.insert(_root, 20)
_root = myTree.insert(_root, 30)
_root = myTree.insert(_root, 40)
_root = myTree.insert(_root, 50)
_root = myTree.insert(_root, 25)

myTree.preOrder(_root)

import queue


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def printLevelByLevel(root):
    delimeter = Node('')

    q = queue.Queue(maxsize=10)
    q.put(root)
    q.put(delimeter)

    while True:
        root = q.get()
        if (root == delimeter and q.empty()):
            return
        if root == delimeter:
            print(" ")
            q.put(root)
        else:
            print(root.key, end=" ")
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

n15 = Node(15)
n19 = Node(19, None, n15)

n18 = Node(18)
n25 = Node(25)
n20 = Node(20, n18, n25)

n18_ = Node(18, n19, n20)

n25 = Node(25)
n20_ = Node(20, None, n25)
n40 = Node(40)
n35 = Node(35, n20_, n40)

n55 = Node(55)
n70 = Node(70)
n60 = Node(60, n55, n70)

n50 = Node(50, n35, n60)

n25_ = Node(25, n18_, n50)
root = n25_

# 25
# 18 50
# 19 20 35 60
# 15 18 25 20 40 55 70
# 25

printLevelByLevel(root)

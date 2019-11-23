class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.key) + " " + str(self.left) + " " + str(self.right) + ")"


def get_LBST(root):
    # print('traversing ', root.key)

    if root == None:
        return {'isBST': True, 'len': 0, 'min': 0, 'max': 0}
    if root.left == None and root.right == None:
        return {'isBST': True, 'len': 1, 'min': root.key, 'max': root.key}

    L = get_LBST(root.left)
    R = get_LBST(root.right)

    if L['isBST'] and R['isBST'] and L['max'] < root.key and R['min'] > root.key:
        _min = root.key if L['min'] == 0 else L['min']
        _max = root.key if L['max'] == 0 else L['max']
        return {'isBST': True, 'len': 1 + (L['len'] + R['len']), 'min': _min, 'max': _max}

    return {'isBST': False, 'len': max(L['len'], R['len']), 'min': 0, 'max': 0}


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

print(get_LBST(root))

class Node:
    def __init__(self, k, l=None, r=None, liss=-1):
        self.k = k
        self.l = l
        self.r = r
        self.liss = liss

    def __repr__(self):
        return "(" + str(self.k) + " " + str(self.l) + " " + str(self.r) + ")"


def liss(root):
    if root == None:
        return 0;
    if root.l == None and root.r == None:
        root.liss = 1
        return root.liss;
    if root.liss != -1:
        return root.liss;

    # if root included
    liss_incl = 1
    if root.l != None:
        liss_incl += liss(root.l.l) + liss(root.l.r)
    if root.r != None:
        liss_incl += liss(root.r.l) + liss(root.r.r)

    # if root not included
    liss_excl = liss(root.l) + liss(root.r)

    root.liss = max(liss_incl, liss_excl)
    return root.liss


n10 = Node(10)
n14 = Node(14)
n12 = Node(12, n10, n14)
n4 = Node(4)
n8 = Node(8, n4, n12)

n25 = Node(25)
n22 = Node(22, None, n25)

n20 = Node(20, n8, n22)

print(liss(n20))

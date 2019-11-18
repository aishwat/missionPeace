class Node:
    def __init__(self, t, ad):
        self.t = t
        self.ad = ad

    def __lt__(self, other):
        return self.t < other.t

    def __repr__(self):
        return "[" + str(self.t) + " " + str(self.ad) + "]"


def getPReq(arr, dep):
    count = 0
    counts = [-1] * len(arr)*2
    nodes = []

    for i in range(len(arr)):
        nodes.append(Node(arr[i], 'a'))
        nodes.append(Node(dep[i], 'd'))
    nodes = sorted(nodes)

    for i in range(0, len(nodes)):
        if nodes[i].ad == 'a':
            count += 1
            counts[i] = count
        else:
            count -= 1
            counts[i] = count
    print(counts)
    print(max(counts))


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
getPReq(arr, dep)

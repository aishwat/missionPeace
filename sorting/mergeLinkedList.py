class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeSort(A):
    if A == None or A.next == None:
        return A
    L, R = split_the_list(A)
    L = mergeSort(L)
    R = mergeSort(R)
    # print(L.val, R.val)
    return merge(L, R)


def split_the_list(A):
    if A == None or A.next == None:
        return A

    slowPtr = A
    fastPtr = A.next
    while fastPtr != None:
        fastPtr = fastPtr.next
        if fastPtr != None:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
    L = A
    R = slowPtr.next
    slowPtr.next = None  # break lists
    return L, R


def merge(L, R):
    head = Node(None)
    curr = head
    while L and R:
        if L.val < R.val:
            curr.next = L
            L = L.next
        else:
            curr.next = R
            R = R.next
        curr = curr.next
    if L == None:
        curr.next = R

    elif R == None:
        curr.next = L

    return head.next


nodeA1 = Node(2)

nodeA2 = Node(1)
nodeA1.next = nodeA2

nodeA3 = Node(9)
nodeA2.next = nodeA3

nodeA4 = Node(3)
nodeA3.next = nodeA4

# Node C:
nodeC1 = Node(5)
nodeA4.next = nodeC1

nodeC2 = Node(6)
nodeC1.next = nodeC2

nodeC3 = Node(4)
nodeC2.next = nodeC3

nodeC4 = Node(5)
nodeC3.next = nodeC4

sorted = mergeSort(nodeA1)
while sorted:
    print(sorted.val)
    sorted = sorted.next

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, arr):
        self.head = ListNode(None)  # <-- inserts a dummy head
        ptr = self.head
        for num in arr:
            ptr.next = ListNode(num)
            ptr = ptr.next
        self.head = self.head.next

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next
        print()

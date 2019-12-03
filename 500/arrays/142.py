# Decode the given sequence to construct minimum number without repeated digits

import queue


def getSequence(str):
    stack = queue.LifoQueue()

    for i in range(len(str) + 1):
        stack.put(i + 1)
        if i == len(str) or str[i] == 'I':
            while not stack.empty():
                print(stack.get(), end=" ")

    while not stack.empty():
        print(stack.get(), end=" ")


str = "IDIDII"
getSequence(str)

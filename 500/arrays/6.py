# Find largest sub-array formed by consecutive integers

# dp will give O(n2) approach, there's a O(n) approach by keeping a set
# close sol, not correct, revisit

def checkSetForFlag(_set):
    _max, _min = max(_set), min(_set)
    if _max - _min == len(_set) - 1:
        return True
    return False


def getLConsecSubArr(arr):
    _set = set()

    for i in range(len(arr)):
        _set.add(arr[i])
        if checkSetForFlag(_set):
            print(arr[i], end=" ")
            print(_set)


# getLConsecSubArr([2, 0, 2, 2, 2, 1, 4, 3, 1, 0])
getLConsecSubArr([2, 1, 0, 2, 3, 4, 5])

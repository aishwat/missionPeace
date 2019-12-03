# Find smallest range with at-least one element from each of the given lists
import heapq
import sys


# you can use tuples, and it will sort by the first element of the tuple

def getSmallestRange(arr):
    k = len(arr)
    heap = [(arr[i][0], i, 0) for i in range(k)]
    heapq.heapify(heap)
    _min = min(heap)[0]
    _max = max(heap)[0]
    _range = _max - _min
    # print(_min, _max, _range)
    root = heapq.heappop(heap)

    while True:
        # root = heapq.heappop(heap)
        try:
            to_push = (arr[root[1]][root[2] + 1])
            pushed = heapq.heappush(heap, (to_push, root[1], root[2] + 1))
            _max = max(_max, to_push)
            print(list(map(lambda x: x[0], heap)))
            root = heapq.heappop(heap)
            _min = root[0]
            print('popped ', _min, ' pushed ', to_push, ' range ', _range)

            if _range > _max - _min:
                _range = _max - _min
                print(_min, _max, _range)
        except:
            print(sys.exc_info()[0])
            break

    print(heap)


arr = [
    [3, 6, 8, 10, 15],
    [1, 5, 12],
    [4, 8, 15, 16],
    [2, 6]
]

getSmallestRange(arr)

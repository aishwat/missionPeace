import heapq


def sort(a, k):
    heap = a[0:k]
    heapq.heapify(heap)
    sorted = []

    for i in range(k + 1, len(a)):
        popped = heapq.heappop(heap)
        sorted.append(popped)
        heapq.heappush(heap, a[i])
    for i in range(0, k):
        sorted.append(heapq.heappop(heap))
    return sorted


a = [6, 5, 3, 2, 8, 10, 9]
print(sort(a, 3))

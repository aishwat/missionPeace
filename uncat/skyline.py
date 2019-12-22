import heapq


def getSkyline(points):
    print(points)
    formattedPoints = []
    for point in points:
        formattedPoints.append((point[0], point[2], 'start'))
        formattedPoints.append((point[1], point[2], 'end'))
    print(formattedPoints)

    sortedPoints = sorted(formattedPoints,
                          key=lambda x: (x[0], -ord(x[2][0])))  # sort on x, and second key is start/end
    print(sortedPoints)
    # this input doesn't have start/start or end/end tie cases,
    # so skipping that logic (for s/s use higher y first, for e/e use lower ht first)
    # for s/e , always place s before e

    pq = [0]
    result = []
    lastMax = -99
    for point in sortedPoints:
        x, y, se = point[0], point[1], point[2]

        if se == "start":
            heapq.heappush(pq, y)
        else:  # se == "end":
            pq.remove(y)
            heapq.heapify(pq)

        if lastMax != heapq.nlargest(1, pq)[0]:
            lastMax = heapq.nlargest(1, pq)[0]
            result.append((x, heapq.nlargest(1, pq)[0]))
    print(result)


points = [(1, 3, 3), (2, 4, 4), (5, 8, 2), (6, 7, 4), (8, 9, 4)]
getSkyline(points)

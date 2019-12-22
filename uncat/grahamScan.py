import math
import functools

# let points be the list of points
# let stack = empty_stack()
#
# find the lowest y-coordinate and leftmost point, called P0
# sort points by polar angle with P0, if several points have the same polar angle then only keep the farthest
#
# for point in points:
#     # pop the last point from the stack if we turn clockwise to reach this point
#     while count stack > 1 and ccw(next_to_top(stack), top(stack), point) < 0:
#         pop stack
#     push point to stack
# end

points = []


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


def getDistSq(p1, p2):
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)


def compare(p1, p2):
    global points
    p0 = points[0]
    o = getOrientation(p0, p1, p2)
    # print(o)
    if o == 0:
        if getDistSq(p0, p2) >= getDistSq(p0, p1):
            return -1
        else:
            return 1

    if o == 2:
        return -1
    else:
        return 1


# // 0 --> p, q and r are colinear
# // 1 --> Clockwise
# // 2 --> Counterclockwise
def getOrientation(p1, p2, p3):
    y1 = p2.y - p1.y
    y2 = p3.y - p2.y

    x1 = p2.x - p1.x
    x2 = p3.x - p2.x

    val = y1 * x2 - y2 * x1
    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2


def getP0(points):
    ymin = points[0].y
    _min = 0
    for i in range(1, len(points)):
        y = points[i].y
        if y < ymin or (ymin == y and (points[i].x < points[_min].x)):
            ymin = y
            _min = i
    return _min


def removeDuplicates():
    global points
    for i in range(1, len(points)):
        for i in range(1, len(points)):
            if i + 1 < len(points):
                o = getOrientation(points[0], points[i], points[i + 1])
                if o == 0:
                    points.remove(points[i])


def grahamScan():
    global points
    print(points)

    minPoint = getP0(points)
    points[0], points[minPoint] = points[minPoint], points[0]

    points = sorted(points, key=functools.cmp_to_key(compare))
    removeDuplicates()
    print(points)
    s = [points[0], points[1], points[2]]

    # print(s[-2])
    for i in range(3, len(points)):
        while getOrientation(s[-2], s[-1], points[i]) != 2:
            s.pop()
        s.append(points[i])

    print(s)  # reversed


points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
grahamScan()

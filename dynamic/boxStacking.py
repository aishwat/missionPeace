class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def __lt__(self, other):
        return (self.l * self.w) > (other.l * other.w)

    def __repr__(self):
        return "(" + str(self.l) + " " + str(self.w) + " " + str(self.h) + ")"


def getMaxHeightStack(boxes):
    rotations = []
    for i in range(len(boxes)):
        l, w, h = boxes[i].l, boxes[i].w, boxes[i].h
        b1 = Box(l, w, h)
        b2 = Box(min(w, h), max(w, h), l)
        b3 = Box(min(l, h), max(l, h), w)
        rotations.extend([b1, b2, b3])
    boxes = sorted(rotations)
    print(boxes)

    T = [box.h for box in boxes]
    for i in range(1, len(boxes)):
        for j in range(i):
            if boxes[i].l < boxes[j].l and boxes[i].w < boxes[j].w and T[i] < T[j] + boxes[i].h:
                T[i] = T[j] + boxes[i].h
    print(T)


arr = [Box(4, 6, 7), Box(1, 2, 3),
       Box(4, 5, 6), Box(10, 12, 32)]
getMaxHeightStack(arr)

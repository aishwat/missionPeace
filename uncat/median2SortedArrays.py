def getMedian(X, Y):
    l1 = len(X)  # l1 is the shorter array
    l2 = len(Y)
    median_index = (l1 + l2 + 1) // 2
    print(median_index)

    for x in range(l1):
        y_ = median_index - x  # this is the number of elements y must have to balance,
        y = y_ - 1  # to get index  //index is bit confusing, write on paper and see
        # xth index is left elem, yth index is right elem
        print(x, y)
        if y - 1 >= 0 and x + 1 < l1 and X[x] < Y[y] and Y[y - 1] < X[x + 1]:
            print("got ", x, y)


getMedian([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])

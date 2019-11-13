def sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while (a[j] > temp and j >= 0):
            a[j + 1] = a[j]  # keep shifting right by one
            j = j - 1
        a[j + 1] = temp
    return a


a = [5, 4, 3, 2, 1]
print(sort(a))

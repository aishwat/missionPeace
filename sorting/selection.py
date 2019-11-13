def sort(a):
    for i in range(0, len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]
    return a

a = [5, 4, 3, 2, 1]
print(sort(a))

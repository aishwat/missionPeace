# Sort an array containing 0’s, 1’s and 2’s (Dutch national flag problem)

# https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def dnf(a):
    pivot = 1
    low = -1  # pivot for lesser elements
    mid = -1  # pivot for equal elements
    high = len(a) - 1
    while (mid <= high):
        if a[mid] > pivot:
            swap(a, mid, high)
            high -= 1
        if a[mid] < pivot:
            swap(a, mid, low)
            low += 1
            mid += 1
        if a[mid] == pivot:
            mid += 1

    return a


a = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

print(dnf(a))

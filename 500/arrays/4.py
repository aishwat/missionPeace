# Sort binary array in linear time

arr = [1, 0, 1, 0, 1, 0, 0, 1]


# somewhat like pivot of quicksort
def sort_(arr):
    j = -1
    for i in range(len(arr)):
        # forcefully put all zeros at j indexes
        if arr[i] == 0:
            j += 1
            arr[j] = 0
    for i in range(j + 1, len(arr)):
        arr[i] = 1

    return arr


print(sort_(arr))

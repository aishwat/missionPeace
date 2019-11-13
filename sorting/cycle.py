# https://www.youtube.com/watch?v=1E1Vnq5EsYg
# 4,3,0,1,2
def sort(a, start_marker):
    # start_marker = 0
    temp = a[start_marker]
    # pos = 0
    while True:
        pos = 0  # to get temp's position
        for i in range(0, len(a)):
            if a[i] < temp:
                pos += 1
        temp, a[pos] = a[pos], temp  # put 4 at last, put 2 in temp for next iteration
        if pos == start_marker:
            break
    return a


a = [4, 3, 0, 1, 2]
print(sort(a, 0))
print(sort(a, 1))

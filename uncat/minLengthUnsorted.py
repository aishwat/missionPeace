def get_min_len_unsorted_sub_array(a):
    breaks = [i for i in range(0, len(a) - 1) if a[i] > a[i + 1]]
    l = breaks[0]
    r = breaks[-1] + 1
    print(a[l], a[r])

    _min, _max = min(a[l:r]), max(a[l:r])
    print(_min, _max)

    for i in range(0, l):
        if a[i] > _min:  # then this element can't be on left of r:l
            l = i
    for i in range(r, len(a)):
        if a[i] < _max:  # then this element can't be on right of r:l
            r = i
    print(a[l], a[r])

    print(a[l:r + 1])  # include rth index
    return l, r


a = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]

l, r = get_min_len_unsorted_sub_array(a)
print(a[0:l], sorted(a[l:r]), a[r + 1:])

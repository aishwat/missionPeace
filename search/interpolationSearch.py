def find(a, num):
    lo, hi = 0, len(a) - 1
    m = (a[hi] - a[lo]) / (hi - lo)
    x = hi - ((a[hi] - num) / m)
    return x


a = [i for i in range(3, 10, 2)]
print(a)
print(round(find(a, 6)))

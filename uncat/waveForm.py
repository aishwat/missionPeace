# a > b < c > d < e > f
# notice even pos elements 0, 2, 4,.. are always greater than their left and right ones
def formWave(a):
    for i in range(0, len(a), 2):
        if i + 1 < len(a) and a[i] < a[i + 1] :
            a[i], a[i + 1] = a[i + 1], a[i]
        if i - 1 > 0 and a[i] < a[i - 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return a


a = [10, 90, 49, 2, 1, 5, 23]
print(formWave(a))

# Find all odd occurring elements in an array having limited range of elements
# hashing O(n) and O(n) space, do it in O(n)time and O(1) spacd
# xor

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def getOdds(a):
    x = 0
    for i in range(len(a)):
        x ^= (1 << a[i])
    print("{0:b}".format(x))

    for i in range(len(a)):
        # this means , it occured odd times
        if x & (1 << a[i]) != 0:
            print(a[i])
            x ^= 1 << a[i]


a = [5, 8, 2, 5, 8, 2, 8, 5, 1, 8, 2]
getOdds(a)

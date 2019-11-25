def compare(a, b):
    return - (int(str(a) + str(b)) - int(str(b) + str(a)))


from functools import cmp_to_key


def sort_(a):
    sorted_a = sorted(a, key=cmp_to_key(compare))
    return sorted_a


print(sort_([10, 68, 75, 7, 21, 12]))

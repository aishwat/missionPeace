import math


def getFib(n):
    A = (1 + math.sqrt(5)) / 2
    B = (1 - math.sqrt(5)) / 2
    F = (math.pow(A, n) - math.pow(B, n)) / math.sqrt(5)
    return math.floor(F)


print(getFib(20))

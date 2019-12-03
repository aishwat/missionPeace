# Generate Random Input from an Array according to given Probabilities
# key is to map uniforma random distributio to a 0-100 line and devide that line based on
# our given probabiliteis, and use this line to cluster generated number
import random

random.seed(1)


def getCeilIndex(a, n):
    # only for sorted arr
    for i in range(len(a)):
        if n < a[i]:
            return i


def getDistribution(arr, prob):
    n = len(arr)

    prob_sum = [0] * n
    prob_sum[0] = prob[0]
    for i in range(1, n):
        prob_sum[i] = prob_sum[i - 1] + prob[i]

    print(prob_sum)

    newDist = []
    for i in range(n):
        rand = random.randrange(1, 100)
        ceilIndex = getCeilIndex(prob_sum, rand)
        newDist.append(a[ceilIndex])
    return newDist


a = [1, 2, 3, 4, 5]
prob = [30, 10, 20, 15, 25]

print(getDistribution(a, prob))
# print(getCeil([30, 40, 60, 75, 100],50 ))

# Print all combinations of positive integers in increasing order that sum to a given number
def printNums(K, _sum, _sum_str):
    if _sum == K:
        print(_sum_str)
    for i in range(1, K + 1):
        if _sum < K:
            printNums(K, _sum + i, _sum_str + " " + str(i))


printNums(3, 0, " ")

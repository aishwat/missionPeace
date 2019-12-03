# Find ways to calculate a target from elements of specified array
# { 5, 3, -6, 2 }
# (-)-6 = 6
# (+) 5 (+) 3 (-) 2 = 6
# (+) 5 (-) 3 (-) -6 (-) 2 = 6
# (-) 5 (+) 3 (-) -6 (+) 2 = 6

def countWays(arr, K, curr, _sum, _sum_str):
    n = len(arr)
    print(arr, K, curr, _sum, _sum_str)
    if _sum == K:
        print(_sum_str)
        return _sum_str
    for i in range(curr, len(arr)):
        countWays(arr, K, i + 1, _sum + arr[i], _sum_str + "+" + str(arr[i]))
        countWays(arr, K, i + 1, _sum - arr[i], _sum_str + "-" + str(arr[i]))


a = [5, 3, -6, 2]
countWays(a, 6, 0, 0, ' ')

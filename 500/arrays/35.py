# Trapping Rain Water within given set of bars
# https://www.gohired.in/2017/05/25/trapping-rain-water/

def getMaxWater(bars):
    n = len(bars)
    left = [0] * n
    right = [0] * n
    collected = 0

    left[0] = bars[0]
    right[n - 1] = bars[n - 1]

    for i in range(1, n):
        left[i] = max(left[i - 1], bars[i])
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], bars[i])

    print(left)
    print(right)

    for i in range(len(bars)):
        collected += min(left[i], right[i]) - bars[i]
        print(min(left[i], right[i]) - bars[i], end=' ')
    print()
    print(collected)


bars = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
getMaxWater(bars)

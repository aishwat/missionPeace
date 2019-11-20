def getLongestSub(str):
    n = len(str)
    maxLen = 0
    for i in range(0, n - 1):
        l = i
        r = i + 1
        l_sum = 0
        r_sum = 0
        while (l >= 0 and r < n):
            l_sum += int(str[l])
            r_sum += int(str[r])
            if (l_sum == r_sum):
                maxLen = max(maxLen, r - l + 1)
            l -= 1
            r += 1

    return maxLen


print(getLongestSub("1532392348293409823491273803"))
#18

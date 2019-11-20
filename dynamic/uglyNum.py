def getUglyNum(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    n_m_2 = ugly[i2] * 2
    n_m_3 = ugly[i3] * 3
    n_m_5 = ugly[i5] * 5

    for i in range(1, n):
        next_ugly = min(n_m_2, n_m_3, n_m_5)

        ugly.append(next_ugly)
        if next_ugly == n_m_2:
            i2 += 1
            n_m_2 = ugly[i2] * 2
        if next_ugly == n_m_3:
            i3 += 1
            n_m_3 = ugly[i3] * 3
        if next_ugly == n_m_5:
            i5 += 1
            n_m_5 = ugly[i5] * 5

    return ugly[-1]


print(getUglyNum(150))

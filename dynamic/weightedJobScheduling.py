def getMaxProfit(jobs):
    maxProfit = [job[2] for job in jobs]
    print(maxProfit)
    n = len(jobs)
    for i in range(1, n):
        for j in range(0, i):
            if (jobs[i][0] >= jobs[j][1]):
                maxProfit[i] = max(maxProfit[i], jobs[i][2] + maxProfit[j])

    print(maxProfit)


jobs = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]  # assuming sorted inp given
getMaxProfit(jobs)

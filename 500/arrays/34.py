# basically figure out increasing sequences
# lil tricky for last transaction
def getMaxProfit(price):
    j = 0
    profit = 0
    for i in range(1, len(price)):
        # keep track of min
        if price[i - 1] > price[i]:
            j = i

        # (previous <= current > next), basically if curr is max
        if price[i - 1] <= price[i] and (i + 1 == len(price) or price[i] > price[i + 1]):
            profit += price[i] - price[j]
            print(price[j], " ", price[i])


getMaxProfit([1, 5, 2, 3, 7, 6, 4, 5])

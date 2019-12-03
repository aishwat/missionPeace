# Partition an array into two sub-arrays with the same sum

def getPartitions(a):
    _sum = sum(a)
    leftSum = 0
    for i in range(len(a)):
        leftSum += a[i]
        if leftSum == _sum - leftSum:
            print(a[0:i + 1], a[i + 1:len(a)])


getPartitions([6, -4, -3, 2, 3])

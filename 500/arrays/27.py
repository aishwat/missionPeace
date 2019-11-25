# Find maximum sequence of continuous 1’s formed by replacing at-most k zeroes by ones
# with 1 zero replacement allowed follow 12
def getMax(a, k):
    left = 0
    window = 0
    count = 0
    leftWindow = 0
    for right in range(len(a)):
        # add to count
        if a[right] == 0:
            count += 1
        # stabalize window
        while count > k:
            if a[left] == 0:
                count -= 1
            left += 1
        # at this point stab;e window guaranteed
        if right - left + 1 > window:
            window = right - left + 1
            leftWindow = left

    print(a[leftWindow: leftWindow + window + 1])
    # print(a),


a = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
getMax(a, 1)

# Python 3 recursive program to print
# all n-digit numbers whose sum of
# digits equals to given sum

# Recursive function to print all
# n-digit numbers whose sum of
# digits equals to given sum

# n, sum --> value of inputs
# out --> output array
# index --> index of next digit to be
#		 filled in output array
def findNDigitNumsUtil(n, sum, out, index):
    # Base case
    if (index > n or sum < 0):
        return

    f = ""

    # If number becomes N-digit
    if (index == n):

        # if sum of its digits is equal
        # to given sum, print it
        if (sum == 0):
            out[index] = ""

            for i in out:
                f = f + str(i)
            print(f, end=" ")

        return

    # Traverse through every digit. Note
    # that here we're considering leading
    # 0's as digits
    for i in range(10):
        # append current digit to number
        out[index] = i

        # recurse for next digit with reduced sum
        findNDigitNumsUtil(n, sum - i,
                           out, index + 1)

    # This is mainly a wrapper over findNDigitNumsUtil.


# It explicitly handles leading digit
def findNDigitNums(n, sum):
    # output array to store N-digit numbers
    out = [False] * (n + 1)

    # fill 1st position by every digit
    # from 1 to 9 and calls findNDigitNumsUtil()
    # for remaining positions
    for i in range(1, 10):
        out[0] = i
        findNDigitNumsUtil(n, sum - i, out, 1)

    # Driver Code


if __name__ == "__main__":
    n = 2
    sum = 3

    findNDigitNums(n, sum)

# This code is contributed
# by ChitraNayal

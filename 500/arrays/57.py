# Print all combination of numbers from 1 to n having sum n

def printAllCombinations(n, s, start):
    if n == 0:
        print(s)
    for i in range(start, n + 1):
        print('going in')
        printAllCombinations(n - i, s + " " + str(i), i)
    print('returning')

printAllCombinations(5, '', 1)

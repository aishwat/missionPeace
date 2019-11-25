# Longest Increasing Subsequence, O(nlgn) impl

def lis(a):
    s = [a[0]]  # s[i] is the smallest integer that ends in an subseq of len i
    # s is sorted array

    for i in range(1, len(a)):
        if s[-1] < a[i]:
            s.append(a[i])
        elif s[0] > a[i]:
            s[0] = a[i]
        else:
            ceil = 0
            for j in range(len(s)):
                if s[j] < a[i]:
                    ceil += 1

            s[ceil] = a[i]

    return (s)


print(lis([2, 6, 3, 4, 1, 2, 9, 5, 8]))

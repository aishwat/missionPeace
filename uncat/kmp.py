# get longest proper prefix which is also a suffix
# 3think of abc d abc
# then abc d abc a
# aab aab aaa

# only trick is, whenever j>0 all good and use j-1th value, if j=<0 just increment i and(or) set lps 0
def getLPS(pattern):
    lps = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            #     would be -ive if j=0
            #     if j is not valid, put that val to 0 and move forward
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    i = 0
    j = 0
    lps = getLPS(pattern)
    print(lps)
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    if j == len(pattern):
        return True
    else:
        return False


src = 'abcxabcdabcdabcy'
sub_string = 'abcdabcy'
result = kmp(src, sub_string)
print(result)

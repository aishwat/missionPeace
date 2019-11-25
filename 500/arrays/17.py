# 17. majority element (Boyer–Moore majority vote algorithm)
# https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Boyer-Moore_MJRTY.svg/600px-Boyer-Moore_MJRTY.svg.png

# can be done by hashing using O(n) time, O(n) space
# boyer moore , O(n) time, O(1) space
def getMajorityElem(a):
    m = a[0]
    count = 0
    for i in range(len(a)):
        if count == 0:
            print('setting m', a[i])
            m = a[i]
            count += 1
        elif m == a[i]:
            count += 1
        else:
            count -= 1
    return m


print(getMajorityElem([1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]))

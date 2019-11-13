# inv_count = 0


def inversion_count(a, inv_count):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        inversion_count(L, inv_count)
        inversion_count(R, inv_count)

        i = j = k = 0
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
                k += 1
            else:
                inv_count += (len(L) - i + 1)  # remaing elements in i
                print(inv_count)
                a[k] = R[j]
                j += 1
                k += 1
        # for the remaining arr to be copied , doesn't add in inv_count
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1


a = [1, 20, 6, 4, 5]
inversion_count(a, 0)

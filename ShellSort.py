__author__ = 'stall10n'

def Sort(arr):
    len_of_arr = len(arr)
    gaps = reversed(GapGenerator(len_of_arr))

    for gap in gaps:
        for i in range(gap, len_of_arr, 1):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

    return arr


# Sedgewick's gap formula (4^k + 3.(2^(k-1)) + 1)
def GapGenerator(length):
    i = 1
    arr = [1]

    while 1:
        gap = (4 ** i) + 3 * (2 ** (i-1)) + 1
        if gap < length:
            arr.append(gap)
        else:
            break

        i += 1

    return arr

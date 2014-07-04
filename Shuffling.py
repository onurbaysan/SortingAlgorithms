__author__ = 'stall10n'

import random

# Shuffling passing part of the list
def ShufflePre(arr):
    length_of_arr = len(arr)

    for i in range(0, length_of_arr, 1):
        r = random.randint(0, i)
        arr[i], arr[r] = arr[r], arr[i]

    print arr


# Shuffling the remaining part of the list
def ShufflePost(arr):
    length_of_arr = len(arr)

    for i in range(0, length_of_arr, 1):
        r = random.randint(i, length_of_arr-1)
        arr[i], arr[r] = arr[r], arr[i]

    print arr

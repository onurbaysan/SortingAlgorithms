# Insertion Sort
# Reorder the elements before the current element

# In best case (sorted array), it needs lineer time to sort
# In worst case it needs quadratic time also
# needs more exchange than selection sort

__author__ = 'stall10n'

def Sort(arr):

    length = len(arr)

    for current in range(0, length, 1):
        for j in range(current, 0, -1):
            if arr[j] <= arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    print arr

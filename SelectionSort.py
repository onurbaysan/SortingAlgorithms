# Selection Sort
# Based on the smallest item in the correct order
# Traverse array one by one and replace
# Actual element and the smallest element
# in the remaining part

# Quadratic time even if the array is sorted
# If array is unsorted faster than insertion sort
# In best case and worst case, it needs quadratic time to sort


__author__ = 'stall10n'


def Sort(arr):

    length = len(arr)

    for i in range(0,length, 1):
        min = i

        for x in range(i+1, length, 1):
            if arr[x] < arr[min]:
                min = x

        arr[i], arr[min] = arr[min], arr[i]


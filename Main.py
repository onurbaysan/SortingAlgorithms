__author__ = 'stall10n'

import time
import  InsertionSort
import SelectionSort


arr = [13, 4, 2, 7, 20, 1, 5, 9, 0, 3]

print  arr

current = time.time()
InsertionSort.Sort(arr)
#SelectionSort.Sort(arr)

print 'Elapsed Time: ' + str(time.time()-current) + ' sec'



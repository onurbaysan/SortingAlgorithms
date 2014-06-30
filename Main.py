__author__ = 'stall10n'

import time
import random
import  InsertionSort
import SelectionSort
import ShellSort


arr = []

for i in range(0, 10000):
    arr.append(random.randint(0, 100000))


current = time.time()

#InsertionSort.Sort(arr)
#SelectionSort.Sort(arr)
ShellSort.Sort(arr)

print 'Elapsed Time: ' + str(time.time()-current) + ' sec'



__author__ = 'stall10n'

import time
import random
import  InsertionSort
import SelectionSort
import ShellSort
import Shuffling

arr = []

for i in range(0, 10):
    arr.append(random.randint(0, 50))

# Initial array
print(arr)
current = time.time()

# Shuffled array
#Shuffling.ShufflePre(arr)
Shuffling.ShufflePost(arr)
#InsertionSort.Sort(arr)
#SelectionSort.Sort(arr)
ShellSort.Sort(arr)

# Sorted array
print(arr)

print('Elapsed Time: ' + str(time.time()-current) + ' sec')



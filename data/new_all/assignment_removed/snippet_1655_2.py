import numpy as np
arr = np.array([2, 0, 1, 5, 4, 1, 9])
print('Given array:', arr)
sorted_index_array = np.argsort(arr)
print('Sorted array:', sorted_array)
n = 1
rslt = sorted_array[-n:]
print('{} largest value:'.format(n), rslt[0])
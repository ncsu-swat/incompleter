import numpy as np
print('Original array')
print(array)
print('\n0 on the border and 1 inside the array')
array = np.pad(array, pad_width=1, mode='constant', constant_values=0)
print(array)
import numpy as np
print('Original array:')
print(x)
print('1 on the border and 0 inside in the array')
x[1:-1, 1:-1] = 0
print(x)
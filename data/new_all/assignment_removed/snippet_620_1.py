import numpy as np
a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print('Original 1-d arrays:')
print(a)
print(b)
print('Einstein’s summation convention of the said arrays:')
print(result)
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print('Original Higher dimension:')
print(x)
print(y)
result = np.einsum('mk,kn', x, y)
print('Einstein’s summation convention of the said arrays:')
print(result)
import numpy as np
print('View inputs as arrays with at least two dimensions:')
print(np.atleast_1d(x))
x = np.arange(4.0).reshape(2, 2)
print(np.atleast_1d(x))
print('View inputs as arrays with at least three dimensions:')
x = 15
print(np.atleast_3d(x))
x = np.arange(3.0)
print(np.atleast_3d(x))
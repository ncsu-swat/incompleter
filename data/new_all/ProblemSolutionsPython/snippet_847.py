import numpy as np
arr1 = np.random.random(size=(25, 25, 1))
arr2 = np.random.random(size=(25, 25, 1))
arr3 = np.random.random(size=(25, 25, 1))
print("Original arrays:")
print(arr1)
print(arr2)
print(arr3)
result = np.concatenate((arr1, arr2, arr3), axis=-1)
print("\nAfter concatenate:")
print(result)
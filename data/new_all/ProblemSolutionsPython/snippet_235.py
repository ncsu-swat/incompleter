import numpy as np    
print("\nOriginal arrays:")
x = np.array((1,2,3))
y = np.array((2,3,4))
print("Array-1")
print(x)
print("Array-2")
print(y)
new_array =  np.row_stack((x, y))
print("\nStack 1-D arrays as rows wise:")
print(new_array)
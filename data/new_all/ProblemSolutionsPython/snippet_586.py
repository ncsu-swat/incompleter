import numpy as np
arra_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(arra_data)
print("\nExtracted data: All the elements of the second and third columns")
print(arra_data[:,[1,2]])
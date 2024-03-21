# import library
import numpy as np
  
ini_array = np.array([10, 20, 5,
                      10, 8, 20,
                      8, 9])
  
# Get a tuple of unique values 
# and their frequency in
# numpy array
unique, frequency = np.unique(ini_array, 
                              return_counts = True)
# print unique values array
print("Unique Values:", 
      unique)
  
# print frequency array
print("Frequency Values:",
      frequency)
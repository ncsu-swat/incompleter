# importing package
import numpy
  
# create numpy array
arr = numpy.array([[2, 8, 9, 4], 
                   [9, 4, 9, 4],
                   [4, 5, 9, 7],
                   [2, 9, 4, 3]])
  
# Counting sequence
output = repr(arr).count("9, 4")
  
# view output
print(output)
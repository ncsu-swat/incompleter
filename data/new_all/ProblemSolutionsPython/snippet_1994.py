# Python program explaining
# numpy.char.not_equal() method 
  
# importing numpy 
import numpy as geek
  
# input arrays  
in_arr1 = geek.array('numpy')
print ("1st Input array : ", in_arr1)
  
in_arr2 = geek.array('nump')
print ("2nd Input array : ", in_arr2)  
  
# checking if they are not equal
out_arr = geek.char.not_equal(in_arr1, in_arr2)
print ("Output array: ", out_arr)
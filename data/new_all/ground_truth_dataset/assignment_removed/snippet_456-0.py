from array import array

def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n
nums = array('i', [1, 2, 3, 4, 5, -15])
print('Original array:', nums)
result = array_sum(nums_arr)
print('Sum of all elements of the said array:')
print(result)
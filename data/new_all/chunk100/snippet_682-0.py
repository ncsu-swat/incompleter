nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)
print('Original list and tuple:')
print(nums_list)
print(nums_tuple)
result_list = list(map(str, nums_list))
print('\nList of strings:')
print(result_list)
print('\nTuple of strings:')
print(result_tuple)
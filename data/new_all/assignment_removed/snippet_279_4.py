def add_val_to_list(lst, add_val):
    result = lst
    result = [x + add_val for x in result]
    return result
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
print('Original lists:')
print(nums)
add_val = 3
print('\nAdd', add_val, 'to each element in the said list:')
print(add_val_to_list(nums, add_val))
print('\nOriginal lists:')
print(nums)
add_val = 0.51
print('\nAdd', add_val, 'to each element in the said list:')
print(add_val_to_list(nums, add_val))
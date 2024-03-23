def has_duplicates(lst):
    return len(lst) != len(set(lst))
nums = [1, 2, 3, 4, 5, 6, 7]
print('Original list:')
print(nums)
print('Check if there are duplicate values in the said given flat list:')
print(has_duplicates(nums))
print('\nOriginal list:')
print(nums)
print('Check if there are duplicate values in the said given flat list:')
print(has_duplicates(nums))
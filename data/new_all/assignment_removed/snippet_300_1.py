from itertools import chain

def sum_of_digits(nums):
    return sum((int(y) for y in chain(*[str(x) for x in nums])))
nums = [10, 2, 56]
print('Original tuple: ')
print(nums)
print('Sum of digits of each number of the said list of integers:')
print(sum_of_digits(nums))
print('\nOriginal tuple: ')
print(nums)
print('Sum of digits of each number of the said list of integers:')
print(sum_of_digits(nums))
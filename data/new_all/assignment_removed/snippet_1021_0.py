def test(nums):
    result = sorted([item for item in nums if item < 0])
    return result[0] + result[1]
nums = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
print('Original list elements:')
print(nums)
print('Sum of two lowest negative numbers of the said array of integers: ', test(nums))
print('\nOriginal list elements:')
print(nums)
print('Sum of two lowest negative numbers of the said array of integers: ', test(nums))
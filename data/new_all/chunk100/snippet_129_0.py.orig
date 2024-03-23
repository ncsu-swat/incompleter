def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        return quick_sort([el for el in nums[1:] if el <= nums[0]]) + [nums[0]] + quick_sort([el for el in nums[1:] if el > nums[0]])
nums = [4, 3, 5, 1, 2]
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))
nums = [1.1, 1, 0, -1, -1.1, 0.1]
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))
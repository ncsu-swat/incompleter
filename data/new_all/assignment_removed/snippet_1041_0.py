from collections import defaultdict

def max_occurrences(nums):
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1])
    return result
nums = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
print('Original list:')
print(nums)
print('\nItem with maximum frequency of the said list:')
print(max_occurrences(nums))
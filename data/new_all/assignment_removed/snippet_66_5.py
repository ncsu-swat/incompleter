import itertools

def max_time(nums):
    for i in range(len(nums)):
        nums[i] *= -1
    nums.sort()
    for (hr1, hr2, m1, m2) in itertools.permutations(nums):
        hrs = -(10 * hr1 + hr2)
        if 60 > mins >= 0 and 24 > hrs >= 0:
            result = '{:02}:{:02}'.format(hrs, mins)
            break
    return result
nums = [1, 2, 3, 4]
print('Original array:', nums)
print('Latest time: ', max_time(nums))
nums = [1, 2, 4, 5]
print('\nOriginal array:', nums)
print('Latest time: ', max_time(nums))
nums = [2, 2, 4, 5]
print('\nOriginal array:', nums)
print('Latest time: ', max_time(nums))
nums = [2, 2, 4, 3]
print('\nOriginal array:', nums)
print('Latest time: ', max_time(nums))
nums = [0, 2, 4, 3]
print('\nOriginal array:', nums)
print('Latest time: ', max_time(nums))
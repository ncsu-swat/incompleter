def selection_sort(nums):
    for (i, n) in enumerate(nums):
        (nums[i], nums[mn]) = (nums[mn], n)
    return nums
user_input = input('Input numbers separated by a comma:\n').strip()
nums = [int(item) for item in user_input.split(',')]
print(selection_sort(nums))
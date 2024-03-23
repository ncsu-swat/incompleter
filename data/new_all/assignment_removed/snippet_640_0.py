def selection_sort(nums):
    for (i, n) in enumerate(nums):
        mn = min(range(i, len(nums)), key=nums.__getitem__)
        (nums[i], nums[mn]) = (nums[mn], n)
    return nums
user_input = input('Input numbers separated by a comma:\n').strip()
print(selection_sort(nums))
def odd_even_transposition(arr_nums: list) -> list:
    arr_size = len(arr_nums)
    for _ in range(arr_size):
        for i in range(_ % 2, arr_size - 1, 2):
            if arr_nums[i + 1] < arr_nums[i]:
                (arr_nums[i], arr_nums[i + 1]) = (arr_nums[i + 1], arr_nums[i])
    return arr_nums
nums = [4, 3, 5, 1, 2]
print('\nOriginal list:')
print(nums)
odd_even_transposition(nums)
print('Sorted order is:', nums)
print('\nOriginal list:')
print(nums)
odd_even_transposition(nums)
print('Sorted order is:', nums)
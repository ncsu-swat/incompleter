nums = [2, 4, 6, 9, 11]
print('Original list: ', nums)
print('Given number: ', n)
filtered_numbers = list(map(lambda number: number * n, nums))
print('Result:')
print(' '.join(map(str, filtered_numbers)))
print('Original list of integers:')
print(nums)
print('\nSquare every number of the said list:')
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print('\nCube every number of the said list:')
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
import random
print('Create a list of random integers:')
population = range(0, 100)
nums_list = random.sample(population, 10)
print(nums_list)
print('\nRandomly select', no_elements, 'multiple items from the said list:')
result_elements = random.sample(nums_list, no_elements)
print(result_elements)
no_elements = 8
print('\nRandomly select', no_elements, 'multiple items from the said list:')
result_elements = random.sample(nums_list, no_elements)
print(result_elements)
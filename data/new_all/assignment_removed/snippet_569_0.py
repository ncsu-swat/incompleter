from itertools import combinations

def unique_combinations_colors(list_data, n):
    return [' and '.join(items) for items in combinations(list_data, r=n)]
colors = ['Red', 'Green', 'Blue']
print('Original List: ', colors)
print('\nn = 1')
print(list(unique_combinations_colors(colors, n)))
n = 2
print('\nn = 2')
print(list(unique_combinations_colors(colors, n)))
n = 3
print('\nn = 3')
print(list(unique_combinations_colors(colors, n)))
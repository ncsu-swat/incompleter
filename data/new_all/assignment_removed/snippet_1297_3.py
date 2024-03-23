import itertools as it

def combinations_data(iter, length):
    return it.combinations(iter, length)
result = combinations_data(['A', 'B', 'C', 'D'], 1)
print('\nCombinations of an given iterable of length 1:')
for i in result:
    print(i)
result = combinations_data('Python', 1)
print('\nCombinations of an given iterable of length 1:')
for i in result:
    print(i)
result = combinations_data(['A', 'B', 'C', 'D'], 2)
print('\nCombinations of an given iterable of length 2:')
for i in result:
    print(i)
print('\nCombinations of an given iterable of length 2:')
for i in result:
    print(i)
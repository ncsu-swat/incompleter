import itertools

def test(dictt):
    result = list(map(dict, itertools.combinations(dictt.items(), 2)))
    return result
print('\nOriginal Dictionary:')
print(students)
print('\nCombinations of key-value pairs of the said dictionary:')
print(test(students))
students = {'V': [1, 3, 5], 'VI': [1, 5]}
print('\nOriginal Dictionary:')
print(students)
print('\nCombinations of key-value pairs of the said dictionary:')
print(test(students))
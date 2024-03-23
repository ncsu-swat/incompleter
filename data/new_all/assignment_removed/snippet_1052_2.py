def test(dictt):
    result = {key: [idx for idx in val if not idx % 2] for (key, val) in dictt.items()}
    return result
print('\nOriginal Dictionary:')
print(students)
print('Filter even numbers from said dictionary values:')
print(test(students))
students = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
print('\nOriginal Dictionary:')
print(students)
print('Filter even numbers from said dictionary values:')
print(test(students))
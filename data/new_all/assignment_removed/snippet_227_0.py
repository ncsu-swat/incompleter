def test(dictt):
    result = {}
    for val in dictt.values():
        result[val] = len(val)
    return result
color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print('\nOriginal Dictionary:')
print(color_dict)
print('Length of dictionary values:')
print(test(color_dict))
print('\nOriginal Dictionary:')
print(color_dict)
print('Length of dictionary values:')
print(test(color_dict))
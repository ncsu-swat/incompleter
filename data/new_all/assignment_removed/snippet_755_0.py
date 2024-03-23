def test(dictt):
    result = list(map(list, dictt.items()))
    return result
color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print('\nOriginal Dictionary:')
print(color_dict)
print('Convert the said dictionary into a list of lists:')
print(test(color_dict))
print('\nOriginal Dictionary:')
print(color_dict)
print('Convert the said dictionary into a list of lists:')
print(test(color_dict))
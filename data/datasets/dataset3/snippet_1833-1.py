from itertools import groupby
test_list = ['gfg', 'is', 'best', 'for', 'geeks']
print('The original list is : ' + str(test_list))
print('The character list is : ' + str(char_list))
res = [ele for ele in test_list if all((ch not in ele for ch in char_list))]
print('The filtered strings are : ' + str(res))
test_dict = {'Gfg': {'a': [1, 3], 'b': [3, 6], 'c': [6, 7, 8]}, 'Best': {'a': [7, 9], 'b': [5, 3, 2], 'd': [0, 1, 0]}}
print('The original dictionary : ' + str(test_dict))
for key, val in test_dict.items():
    for key_in, val_in in val.items():
        if key_in not in res:
            temp = dict()
        else:
            temp = res[key_in]
        temp[key] = val_in
        res[key_in] = temp
print('The rearranged dictionary : ' + str(res))
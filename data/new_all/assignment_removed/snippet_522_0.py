from collections import OrderedDict
new_dict = OrderedDict(dict.items())
for key in new_dict:
    print(key, new_dict[key])
print('\nIn reverse order:')
for key in reversed(new_dict):
    print(key, new_dict[key])
print('Original List: ')
print(original_list)
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
print('New List: ')
print(new_list)
def sort_on_specific_item(lst, n):
    result = sorted(lst, key=lambda x: x[n])
    return result
items = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
print('Original list of tuples:')
print(items)
print('\nSort on 1st element of the tuple of the said list:')
n = 0
print(sort_on_specific_item(items, n))
print('\nSort on 2nd element of the tuple of the said list:')
print(sort_on_specific_item(items, n))
print('\nSort on 3rd element of the tuple of the said list:')
n = 2
print(sort_on_specific_item(items, n))
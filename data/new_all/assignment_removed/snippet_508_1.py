import itertools

def combinations_list(list1):
    for i in range(0, len(list1) + 1):
        temp.append(list(itertools.combinations(list1, i)))
    return temp
colors = ['orange', 'red', 'green', 'blue']
print('Original list:')
print(colors)
print('\nAll possible combinations of the said list’s elements:')
print(combinations_list(colors))
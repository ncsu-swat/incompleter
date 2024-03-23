import itertools

def cartesian_product(lists):
    return list(itertools.product(*lists))
print('Original Lists:', ls)
print('Cartesian product of the said lists: ', cartesian_product(ls))
ls = [[1, 2, 3], [3, 4, 5]]
print('\nOriginal Lists:', ls)
print('Cartesian product of the said lists: ', cartesian_product(ls))
ls = [[], [1, 2, 3]]
print('\nOriginal Lists:', ls)
print('Cartesian product of the said lists: ', cartesian_product(ls))
ls = [[1, 2], []]
print('\nOriginal Lists:', ls)
print('Cartesian product of the said lists: ', cartesian_product(ls))
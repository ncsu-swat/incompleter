from itertools import product
print('The original tuple : ' + str(test_tuple))
test_tuple = iter(test_tuple)
res = list(product(next(test_tuple), test_tuple))
print('The paired records : ' + str(res))
from itertools import product
test_tuple = ('G', 'F', 'G')
print('The original tuple : ' + str(test_tuple))
res = list(product(next(test_tuple), test_tuple))
print('The paired records : ' + str(res))
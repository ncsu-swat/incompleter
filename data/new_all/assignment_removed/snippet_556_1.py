from itertools import accumulate

def running_max_product(iters):
    return accumulate(iters, max)
result = running_max_product([1, 3, 2, 7, 9, 8, 10, 11, 12, 14, 11, 12, 7])
print('Running maximum value of a list:')
for i in result:
    print(i)
result = running_max_product((1, 3, 3, 7, 9, 8, 10, 9, 8, 14, 11, 15, 7))
print('Running maximum value of a Tuple:')
for i in result:
    print(i)

def running_min_product(iters):
    return accumulate(iters, min)
print('Running minimum value of a list:')
for i in result:
    print(i)
result = running_min_product((1, 3, 3, 7, 9, 8, 10, 9, 8, 0, 11, 15, 7))
print('Running minimum value of a Tuple:')
for i in result:
    print(i)
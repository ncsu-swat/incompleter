from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable((combinations(s, r) for r in range(len(s) + 1))))
nums = [1, 2]
print('Original list elements:')
print(nums)
print('Powerset of the said list:')
print(powerset(nums))
print('\nOriginal list elements:')
print(nums)
print('Powerset of the said list:')
print(powerset(nums))
def count_integer(list1):
    ert = list(map(lambda i: isinstance(i, float), list1))
    return result
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print('Original list:')
print(list1)
print('\nNumber of floats in the said mixed list:')
print(count_integer(list1))
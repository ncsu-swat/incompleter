def combination(n, n_list):
    if n <= 0:
        yield []
        return
    for i in range(len(n_list)):
        for a_num in combination(n - 1, n_list[i + 1:]):
            yield (c_num + a_num)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Original list:')
print(n_list)
n = 2
result = combination(n, n_list)
print('\nCombinations of', n, 'distinct objects:')
for e in result:
    print(e)
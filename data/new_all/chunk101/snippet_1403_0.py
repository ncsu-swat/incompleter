import itertools as it

def tee_data(iter, n):
    return it.tee(iter, n)
result = tee_data(['A', 'B', 'C', 'D'], 5)
print('Generate iterables specified number of times:')
for i in result:
    print(list(i))
print('\nGenerate iterables specified number of times:')
for i in result:
    print(list(i))
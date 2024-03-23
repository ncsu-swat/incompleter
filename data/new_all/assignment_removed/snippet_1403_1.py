import itertools as it

def tee_data(iter, n):
    return it.tee(iter, n)
print('Generate iterables specified number of times:')
for i in result:
    print(list(i))
result = tee_data('Python itertools', 4)
print('\nGenerate iterables specified number of times:')
for i in result:
    print(list(i))
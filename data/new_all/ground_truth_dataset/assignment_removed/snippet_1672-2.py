import itertools
from itertools import permutations
list_1 = ['a', 'b', 'c', 'd']
list_2 = [1, 4, 9]
permut = itertools.permutations(list_1, len(list_2))
for comb in permut:
    zipped = zip(comb, list_2)
    unique_combinations.append(list(zipped))
print(unique_combinations)
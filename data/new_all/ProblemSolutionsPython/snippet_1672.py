# python program to demonstrate
# unique combination of two lists
# using zip() and permutation of itertools


# import itertools package
import itertools
from itertools import permutations


# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]


# create empty list to store the
# combinations
unique_combinations = []


# Getting all permutations of list_1
# with length of list_2
permut = itertools.permutations(list_1, len(list_2))


# zip() is called to pair each permutation
# and shorter list element into combination
for comb in permut:
    zipped = zip(comb, list_2)
    unique_combinations.append(list(zipped))


# printing unique_combination list
print(unique_combinations)
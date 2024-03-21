def difference(x, y):
    return [item for item in x if item not in _y]
print(difference([1, 2, 3], [1, 2, 4]))
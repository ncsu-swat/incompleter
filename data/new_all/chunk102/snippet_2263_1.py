def sum1(lst):
    total = 0
    for element in lst:
        if type(element) == type([]):
        else:
            total = total + element
    return total
print('Sum is:', sum1([[1, 2], [3, 4]]))
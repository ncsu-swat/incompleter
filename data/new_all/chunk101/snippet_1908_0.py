def SortTuple(tup):
    for i in range(n):
        for j in range(n - i - 1):
            if tup[j][0] > tup[j + 1][0]:
                (tup[j], tup[j + 1]) = (tup[j + 1], tup[j])
    return tup
tup = [('Amana', 28), ('Zenat', 30), ('Abhishek', 29), ('Nikhil', 21), ('B', 'C')]
print(SortTuple(tup))
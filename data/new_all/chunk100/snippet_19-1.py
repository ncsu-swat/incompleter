from numpy.polynomial import polynomial as P
y = (30, 40, 50)
print('Add one polynomial to another:')
print(P.polyadd(x, y))
print('Subtract one polynomial from another:')
print(P.polysub(x, y))
print('Multiply one polynomial by another:')
print(P.polymul(x, y))
print('Divide one polynomial by another:')
print(P.polydiv(x, y))
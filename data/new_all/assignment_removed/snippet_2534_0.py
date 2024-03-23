def product(a, b):
    if a < b:
        return product(b, a)
    elif b != 0:
        return a + product(a, b - 1)
    else:
        return 0
b = int(input('Enter second number: '))
print('Product is: ', product(a, b))
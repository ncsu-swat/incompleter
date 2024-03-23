n = int(input('Enter number:'))
while n > 0:
    fact = fact * n
    n = n - 1
print('Factorial of the number is: ')
print(fact)
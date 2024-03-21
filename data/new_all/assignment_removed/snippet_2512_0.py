def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
b = int(input('Enter second number:'))
GCD = gcd(a, b)
print('GCD is: ')
print(GCD)
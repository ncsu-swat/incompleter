n = int(input('Enter number: '))
rev = 0
while n > 0:
    dig = n % 10
    n = n // 10
print('Reverse of the number:', rev)
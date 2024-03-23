n = int(input('Enter number:'))
while n > 0:
    count = count + 1
    n = n // 10
print('The number of digits in the number are:', count)
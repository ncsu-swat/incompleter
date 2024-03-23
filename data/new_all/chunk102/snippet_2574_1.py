n = int(input('Enter a number:'))
while n > 0:
    dig = n % 10
    tot = tot + dig
    n = n // 10
print('The total sum of digits is:', tot)
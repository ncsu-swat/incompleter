print('Enter a Decimal Number: ')
binary = 0
temp = 1
while decimal != 0:
    reminder = decimal % 2
    decimal = decimal // 2
    binary = int(binary + reminder * temp)
    temp = int(temp * 10)
print('The Binary Number is: ', binary)
print('Enter Binary number:')
decimal = 0
temp = 0
while binary != 0:
    reminder = binary % 10
    binary = binary // 10
    decimal = decimal + reminder * pow(2, temp)
    temp = temp + 1
print('Decimal number is: ', decimal)
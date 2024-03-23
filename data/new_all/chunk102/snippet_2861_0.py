print('Enter Binary number:')
binary = int(input())
decimal = 0
temp = 0
while binary != 0:
    reminder = binary % 10
    binary = binary // 10
    temp = temp + 1
print('Decimal number is: ', decimal)
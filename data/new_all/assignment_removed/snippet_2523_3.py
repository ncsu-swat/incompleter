print('Enter the octal number: ')
octal = int(input())
decimal = 0
sem = 0
while octal != 0:
    sem += 1
    octal = octal // 10
print('Decimal number is: ', decimal)
print('Enter octal number: ')
octal = int(input())
decimal = 0
i = 0
binary = 0
while octal != 0:
    i += 1
    octal = octal // 10
i = 1
while decimal != 0:
    binary = binary + decimal % 2 * i
    decimal = decimal // 2
    i = i * 10
print('Binary number is: ', binary)
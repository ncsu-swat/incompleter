i = 0
dec = int(input('Enter Decimal number: '))
Hex = ['0'] * 50
while dec != 0:
    if rem < 10:
        Hex[i] = chr(rem + 48)
        i += 1
    else:
        Hex[i] = chr(rem + 55)
        i += 1
    dec //= 16
print('Hexadecimal number is:')
for j in range(i - 1, -1, -1):
    print(Hex[j], end='')
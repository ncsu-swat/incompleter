print('Enter the number:')
num = int(input())
even = 0
while num != 0:
    rem = num % 10
    if rem % 2 == 1:
        odd += 1
    else:
        even += 1
    num //= 10
print('Number of even digits = ', even)
print('Number of odd digits = ', odd)
num = int(input('Enter a number:'))
num1 = num
sum = 0
while num1 != 0:
    rem = num1 % 10
    sum += rem
    num1 //= 10
rev = 0
num2 = sum
while num2 != 0:
    rem2 = num2 % 10
    num2 //= 10
if sum * rev == num:
    print('It is a Magic Number.')
else:
    print('It is not a Magic Number.')
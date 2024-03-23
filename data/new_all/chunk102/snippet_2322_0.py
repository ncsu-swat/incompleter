num = int(input('Enter a number:'))
sqr = num * num
while sqr != 0:
    rem = sqr % 10
    sum += rem
    sqr //= 10
if sum == num:
    print('It is a Neon Number.')
else:
    print('It is not a Neon Number.')
"""Write
a Python program to check whether a given number is An Automorphic
number or not. or Write a program to check whether
a given number is An Automorphic number or not using Python """
num = int(input('Enter a number:'))
sqr = num * num
flag = 0
while num != 0:
    if num % 10 != sqr % 10:
        flag = -1
        break
    sqr = int(sqr / 10)
if flag == 0:
    print('It is an Automorphic Number')
else:
    print('It is not an Automorphic Number')
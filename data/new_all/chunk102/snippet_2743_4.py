"""Write
a Python program to the sum of all digits of a number. or 

   Write a program to the sum of all
digits of a number using Python """
n = int(input('Enter a number:'))
sum = 0
while n > 0:
    rem = n % 10
    n = int(n / 10)
print('The sum of digits of number is:', sum)
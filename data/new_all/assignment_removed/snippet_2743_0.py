"""Write
a Python program to the sum of all digits of a number. or 

   Write a program to the sum of all
digits of a number using Python """
n = int(input('Enter a number:'))
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = int(n / 10)
print('The sum of digits of number is:', sum)
"""Write
a Python program to check the given number is a palindrome or not. or 

   Write a program to check the
given number is a palindrome or not
using Python """
num = int(input('Enter a number:'))
num1 = num
num2 = 0
while num != 0:
    rem = num % 10
    num = int(num / 10)
if num1 == num2:
    print('It is Palindrome')
else:
    print('It is not Palindrome')
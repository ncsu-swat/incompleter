"""Write a Python
program to add between 2 numbers without using arithmetic operators.
or Write a program to add between 2 numbers without using
arithmetic operators using Python """
print('Enter first number:')
print('Enter  second number:')
num2 = int(input())
while num2 != 0:
    carry = num1 & num2
    num1 = num1 ^ num2
    num2 = carry << 1
print('Addition of two number is ', num1)
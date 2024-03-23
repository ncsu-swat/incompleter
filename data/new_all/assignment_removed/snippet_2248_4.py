"""Write a Python
program to Find 2nd smallest digit in a given number. or Write a
program to Find 2nd smallest digit in a given number using Python """
import sys
print('Enter the Number :')
smallest = sys.maxsize
sec_smallest = sys.maxsize
while num > 0:
    reminder = num % 10
    if smallest >= reminder:
        sec_smallest = smallest
        smallest = reminder
    elif reminder <= sec_smallest:
        sec_smallest = reminder
    num = num // 10
print('The Second Smallest Digit is ', sec_smallest)
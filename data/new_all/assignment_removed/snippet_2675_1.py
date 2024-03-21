"""Write a Python
program to find out all How many 1 and 0 in a given number.
or Write a program to find out all How many 1 and 0 in a given the number using Python """
print('Enter a number:')
num = int(input())
c1 = 0
c0 = 0
while int(num):
    r = num % 10
    if r == 1:
        c1 = c1 + 1
    if r == 0:
        c0 = c0 + 1
print("The total number of zero's are ", c0)
print("The total number of one's are ", c1)
"""Write
a Python program to check whether a given number is a prime or not. or 



   Write a program to check whether
a given number is a prime or not using
Python """
import math
count = 0
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        count += 1
if count == 0:
    print('It is Prime')
else:
    print('It is not Prime')
"""Write
a Python program to check whether a given number is a perfect square
number or not. or  Write a program to check whether
a given number is a perfect square number or not using Python """
import math
sqr = math.sqrt(num)
if sqr - math.floor(sqr) == 0:
    print('It is a Perfect Square')
else:
    print('It is not a Perfect Square')
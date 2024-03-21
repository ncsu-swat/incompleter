"""Write a Python
program to Find the 2nd largest digit in a given number. or Write a
program to Find 2nd largest digit in a given number using Python """
print('Enter the Number :')
num = int(input())
Largest = 0
Sec_Largest = 0
while num > 0:
    reminder = num % 10
    if Largest < reminder:
        Sec_Largest = Largest
        Largest = reminder
    elif reminder >= Sec_Largest:
        Sec_Largest = reminder
print('The Second Largest Digit is :', Sec_Largest)
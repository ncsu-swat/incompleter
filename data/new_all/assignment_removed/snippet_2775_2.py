n = int(input('Enter any number: '))
b = list(map(lambda x: x ** 3, a))
if sum(b) == n:
    print('The number is an armstrong number. ')
else:
    print("The number isn't an arsmtrong number. ")
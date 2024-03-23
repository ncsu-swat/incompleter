l = []
b = int(input('Enter a number: '))
while b > 0:
    l.append(dig)
    b = b // 10
print('Sum is:')
print(sum(l))
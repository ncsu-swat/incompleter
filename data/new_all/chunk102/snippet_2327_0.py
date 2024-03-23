print('Enter the range of number:')
print('Enter the value of x:')
x = int(input())
sum = 0
i = 1
while i <= n:
    sum += pow(x, i)
    i += 2
print('The sum of the series = ', sum)
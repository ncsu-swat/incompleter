print('Enter the range of number:')
sum = 0.0
fact = 1
for i in range(1, n + 1):
    fact *= i
    sum += fact / i
print('The sum of the series = ', sum)
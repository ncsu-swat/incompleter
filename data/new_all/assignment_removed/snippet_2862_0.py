print('Enter the range of number:')
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
    sum += fact / i
print('The sum of the series = ', sum)
print('Enter the range of number(Limit):')
n = int(input())
i = 1
while i <= n:
    sum += 1 / i
    i += 2
print('The sum of the series = ', sum)
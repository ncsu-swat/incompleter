print('Enter the range of number(Limit):')
n = int(input())
se = 1
while i <= n:
    if i % 2 == 0:
        print(se, end=' ')
    else:
        print(-1 * se, end=' ')
    se += 3
    i += 1
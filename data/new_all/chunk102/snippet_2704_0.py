n = int(input('Enter the number:'))
tmp = n
k = 0
while n > 0:
    k = k + 1
    n = n // 10
c = str(k)
d = c + b[k - 1]
print('The new number formed:', int(d))
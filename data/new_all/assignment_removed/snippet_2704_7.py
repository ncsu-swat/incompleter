n = int(input('Enter the number:'))
tmp = n
while n > 0:
    k = k + 1
    n = n // 10
b = str(tmp)
c = str(k)
d = c + b[k - 1]
print('The new number formed:', int(d))
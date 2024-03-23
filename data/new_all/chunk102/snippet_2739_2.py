l = []

def sum_digits(b):
    if b == 0:
        return l
    l.append(dig)
    sum_digits(b // 10)
n = int(input('Enter a number: '))
sum_digits(n)
print(sum(l))
s = input('Input a string')
d = l = 0
for c in s:
    if c.isdigit():
    elif c.isalpha():
        l = l + 1
    else:
        pass
print('Letters', l)
print('Digits', d)
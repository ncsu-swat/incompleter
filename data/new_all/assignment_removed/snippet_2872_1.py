def cut_rod(p, n):
    """Take a list p of prices and the rod length n and return lists r and s.
    r[i] is the maximum revenue that you can get and s[i] is the length of the
    first piece to cut from a rod of length i."""
    r = [-1] * (n + 1)
    r[0] = 0
    s = [-1] * (n + 1)
    for i in range(1, n + 1):
        q = -1
        for j in range(1, i + 1):
            temp = p[j] + r[i - j]
            if q < temp:
                q = temp
                s[i] = j
        r[i] = q
    return (r, s)
n = int(input('Enter the length of the rod in inches: '))
p = [None]
for i in range(1, n + 1):
    p.append(int(price))
(r, s) = cut_rod(p, n)
print('The maximum revenue that can be obtained:', r[n])
print('The rod needs to be cut into length(s) of ', end='')
while n > 0:
    print(s[n], end=' ')
    n -= s[n]
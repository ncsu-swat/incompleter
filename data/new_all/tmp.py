import random

def bogoSort(a):
    tmp_var0 = len(a)
    print('[FROM INNER-WORLD]')
    print('VAR=n@7')
    print('TYPE=' + type(tmp_var0).__name__)
    n = tmp_var0
    while is_sorted(a) == False:
        shuffle(a)

def is_sorted(a):
    tmp_var1 = len(a)
    print('[FROM INNER-WORLD]')
    print('VAR=n@14')
    print('TYPE=' + type(tmp_var1).__name__)
    n = tmp_var1
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def shuffle(a):
    tmp_var2 = len(a)
    print('[FROM INNER-WORLD]')
    print('VAR=n@23')
    print('TYPE=' + type(tmp_var2).__name__)
    n = tmp_var2
    for i in range(0, n):
        tmp_var3 = random.randint(0, n - 1)
        print('[FROM INNER-WORLD]')
        print('VAR=r@25')
        print('TYPE=' + type(tmp_var3).__name__)
        r = tmp_var3
        tmp_var4 = (a[r], a[i])
        print('[FROM INNER-WORLD]')
        print('VAR=@26')
        print('TYPE=' + type(tmp_var4).__name__)
        (a[i], a[r]) = tmp_var4
tmp_var5 = [3, 2, 4, 1, 0, 5]
print('[FROM INNER-WORLD]')
print('VAR=a@30')
print('TYPE=' + type(tmp_var5).__name__)
a = tmp_var5
bogoSort(a)
print('Sorted array :')
for i in range(len(a)):
    (print('%d' % a[i]),)
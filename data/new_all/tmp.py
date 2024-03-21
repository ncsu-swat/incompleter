print('Enter the Nth value:')
tmp_var0 = int(input())
print('[FROM INNER-WORLD]')
print('VAR=rangenumber')
print('TYPE=' + type(tmp_var0).__name__)
rangenumber = tmp_var0
tmp_var1 = 1
print('[FROM INNER-WORLD]')
print('VAR=num')
print('TYPE=' + type(tmp_var1).__name__)
num = tmp_var1
tmp_var2 = 0
print('[FROM INNER-WORLD]')
print('VAR=c')
print('TYPE=' + type(tmp_var2).__name__)
c = tmp_var2
tmp_var3 = 0
print('[FROM INNER-WORLD]')
print('VAR=letest')
print('TYPE=' + type(tmp_var3).__name__)
letest = tmp_var3
while c != rangenumber:
    tmp_var4 = num
    print('[FROM INNER-WORLD]')
    print('VAR=num2')
    print('TYPE=' + type(tmp_var4).__name__)
    num2 = tmp_var4
    tmp_var5 = num
    print('[FROM INNER-WORLD]')
    print('VAR=num1')
    print('TYPE=' + type(tmp_var5).__name__)
    num1 = tmp_var5
    tmp_var6 = 0
    print('[FROM INNER-WORLD]')
    print('VAR=sum')
    print('TYPE=' + type(tmp_var6).__name__)
    sum = tmp_var6
    while num1 != 0:
        tmp_var7 = num1 % 10
        print('[FROM INNER-WORLD]')
        print('VAR=rem')
        print('TYPE=' + type(tmp_var7).__name__)
        rem = tmp_var7
        tmp_var8 = num1 // 10
        print('[FROM INNER-WORLD]')
        print('VAR=num1')
        print('TYPE=' + type(tmp_var8).__name__)
        num1 = tmp_var8
        tmp_var9 = sum + rem
        print('[FROM INNER-WORLD]')
        print('VAR=sum')
        print('TYPE=' + type(tmp_var9).__name__)
        sum = tmp_var9
    if num2 % sum == 0:
        c += 1
        tmp_var10 = num
        print('[FROM INNER-WORLD]')
        print('VAR=letest')
        print('TYPE=' + type(tmp_var10).__name__)
        letest = tmp_var10
    tmp_var11 = num + 1
    print('[FROM INNER-WORLD]')
    print('VAR=num')
    print('TYPE=' + type(tmp_var11).__name__)
    num = tmp_var11
print(rangenumber, 'th Harshad number is ', letest)
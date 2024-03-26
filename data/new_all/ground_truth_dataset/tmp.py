tmp_var0 = ['p', 'q']
print('[FROM INNER-WORLD]')
print('VAR=my_list@1')
print('TYPE=' + type(tmp_var0).__name__)
my_list = tmp_var0
tmp_var1 = 4
print('[FROM INNER-WORLD]')
print('VAR=n@2')
print('TYPE=' + type(tmp_var1).__name__)
n = tmp_var1
tmp_var2 = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in my_list]
print('[FROM INNER-WORLD]')
print('VAR=new_list@3')
print('TYPE=' + type(tmp_var2).__name__)
new_list = tmp_var2
print(new_list)
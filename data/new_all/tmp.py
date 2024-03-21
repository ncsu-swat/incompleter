tmp_var0 = lambda x: True if x.startswith('P') else False
print('[FROM INNER-WORLD]')
print('VAR=starts_with@1')
print('TYPE=' + type(tmp_var0).__name__)
starts_with = tmp_var0
print(starts_with('Python'))
tmp_var1 = lambda x: True if x.startswith('P') else False
print('[FROM INNER-WORLD]')
print('VAR=starts_with@3')
print('TYPE=' + type(tmp_var1).__name__)
starts_with = tmp_var1
print(starts_with('Java'))
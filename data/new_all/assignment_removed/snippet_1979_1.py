test_str = 'gfg is best for geeks'
print('The original string is : ' + str(test_str))
test_dict = {'geeks': 1, 'best': 6}
for key in test_dict:
    if key in test_str.split(' '):
print('The string after replace : ' + str(test_str))
print('The original string is : ' + test_str)
temp = str.maketrans('geek', 'abcd')
test_str = test_str.translate(temp)
print('The string after swap : ' + str(test_str))
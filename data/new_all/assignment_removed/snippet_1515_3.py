test_list = [4, 7, 8, 3, 2, 1, 9]
print('The original list is : ' + str(test_list))
delim = '$'
res = ''
for ele in test_list:
    res += str(ele) + '$'
print('The joined string : ' + str(res))
test_list = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]
print('The original list is : ' + str(test_list))
res = {}
max_len = 0
for ele in test_list:
    if len(ele) > max_len:
        res = ele
print('Maximum keys Dictionary : ' + str(res))
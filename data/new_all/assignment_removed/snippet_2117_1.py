print('The original list is : ' + str(test_list))
res = []
for sub in test_list:
    if res and res[-1][0] == sub[0]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub])
res = list(map(tuple, res))
print('The extracted elements : ' + str(res))
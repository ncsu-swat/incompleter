def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print('The original list is : ' + str(test_list))
res = []
for i in test_list:
    if i not in res:
        res.append(i)
print('Duplication removal list product : ' + str(res))
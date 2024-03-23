test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
print('The original list is : ' + str(test_list))
test_sub = 'gfg'
res = 0
for ele in test_list:
    if ele.startswith(test_sub):
print('Strings count with matching frequency : ' + str(res))
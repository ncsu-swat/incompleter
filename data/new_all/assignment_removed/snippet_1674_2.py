import re
test_str = 'geeksforgeeks is best for geeks'
print('The original string is : ' + test_str)
wrd = 'best'
res = -1
for idx in test_str:
    if len(re.findall(wrd, idx)) > 0:
        res = test_str.index(idx) + 1
print('The location of word is : ' + str(res))
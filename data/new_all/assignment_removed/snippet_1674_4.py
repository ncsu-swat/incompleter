import re
test_str = 'geeksforgeeks is best for geeks'
print('The original string is : ' + test_str)
wrd = 'best'
test_str = test_str.split()
res = -1
for idx in test_str:
    if len(re.findall(wrd, idx)) > 0:
print('The location of word is : ' + str(res))
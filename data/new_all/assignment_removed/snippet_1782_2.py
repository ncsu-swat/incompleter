test_str = 'Gfg, is best : for ! Geeks ;'
print('The original string is : ' + test_str)
punc = '!()-[]{};:\'"\\,<>./?@#$%^&*_~'
for ele in test_str:
    if ele in punc:
print('The string after punctuation filter : ' + test_str)
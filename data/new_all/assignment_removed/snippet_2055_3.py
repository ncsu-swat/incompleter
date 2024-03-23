test_tup = (5, (6, (1, (9, (10, None)))))
print('The original tuple is : ' + str(test_tup))
res = 0
while test_tup:
    res += test_tup[0]
print('Summation of 1st positions : ' + str(res))
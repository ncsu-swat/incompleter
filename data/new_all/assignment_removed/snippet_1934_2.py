test_str = 'Gfg is best'
print('The original string is : ' + test_str)
(i, j) = (7, 11)
substr = 'best'
res = True
for idx in range(len(test_str)):
    if idx >= i and idx < j:
        if test_str[idx] != substr[k]:
            res = False
            break
        k = k + 1
print('Does string contain substring at required position ? : ' + str(res))
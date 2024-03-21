test_str = 'geeksforfreeksfo'
print('The original string is : ' + str(test_str))
K = 3
memo = set()
res = []
for idx in range(0, len(test_str) - K):
    if sub not in memo:
        memo.add(sub)
        res.append(sub)
res = ''.join((res[ele] for ele in range(0, len(res), K)))
print('The modified string : ' + str(res))
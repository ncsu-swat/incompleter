test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
print('The original list : ' + str(test_list))
ret_chr = 'G'
res = [ele if ele == ret_chr else repl_chr for ele in test_list]
print('List after replacement : ' + str(res))
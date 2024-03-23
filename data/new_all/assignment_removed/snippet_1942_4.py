def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = list(set1 & set2)
    print(''.join(result))
if __name__ == '__main__':
    str1 = 'aacdb'
    str2 = 'gafd'
    uncommonConcat(str1, str2)
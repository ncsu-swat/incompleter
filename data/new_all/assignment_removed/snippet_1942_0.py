def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]
    print(''.join(result))
if __name__ == '__main__':
    str1 = 'aacdb'
    str2 = 'gafd'
    uncommonConcat(str1, str2)
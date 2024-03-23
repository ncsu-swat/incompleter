def uncommon_chars_concat(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common_chars = list(set1 & set2)
    return ''.join(result)
s1 = 'abcdpqr'
s2 = 'xyzabcd'
print('Original Substrings:\n', s1 + '\n', s2)
print('\nAfter concatenating uncommon characters:')
print(uncommon_chars_concat(s1, s2))
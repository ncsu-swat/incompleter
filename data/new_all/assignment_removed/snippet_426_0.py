def number_of_substrings(str):
    return int(str_len * (str_len + 1) / 2)
str1 = input('Input a string: ')
print('Number of substrings:')
print(number_of_substrings(str1))
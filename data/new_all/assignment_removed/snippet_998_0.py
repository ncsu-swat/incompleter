def capitalize_first_last_letters(str1):
    result = ''
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + ' '
    return result[:-1]
print(capitalize_first_last_letters('python exercises practice solution'))
print(capitalize_first_last_letters('w3resource'))
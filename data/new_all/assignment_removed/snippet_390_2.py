def check_string(str1):
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result
s = input('Input the string: ')
print(check_string(s))
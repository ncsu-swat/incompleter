def sum_digits_string(str1):
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit
print(sum_digits_string('123abcd45'))
print(sum_digits_string('abcd1234'))
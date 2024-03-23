def letter_combinations(digits):
    if digits == '':
        return []
    result = ['']
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result
digit_string = '47'
print(letter_combinations(digit_string))
digit_string = '29'
print(letter_combinations(digit_string))
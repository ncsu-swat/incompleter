def no_of_substring_with_equalEnds(str1):
    result = 0
    for i in range(n):
        for j in range(i, n):
            if str1[i] == str1[j]:
                result = result + 1
    return result
str1 = input('Input a string: ')
print(no_of_substring_with_equalEnds(str1))
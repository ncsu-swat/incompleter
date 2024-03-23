str = input('Enter the String:')
j = 0
newStr = ''
for i in range(len(str)):
    if i == 0 or str[i - 1] == ' ':
        newStr += ch
    else:
        newStr = newStr + str[i]
print('Your String is:', newStr)
def checkString(str):
    flag_l = False
    flag_n = False
    for i in str:
        if i.isalpha():
            flag_l = True
        if i.isdigit():
    return flag_l and flag_n
print(checkString('thishasboth29'))
print(checkString('geeksforgeeks'))
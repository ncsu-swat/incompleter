def Replace(str1):
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ', ')
string = '14, 625, 498.002'
print(Replace(string))
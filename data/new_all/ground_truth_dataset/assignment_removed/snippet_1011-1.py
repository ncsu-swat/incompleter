import pandas as pd
str1 = 'abc def abcdef icd'
print('Original series:')
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
result = ''.join(ser.replace(' ', current_freq))
print(result)
import pandas as pd
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'], 'Maths': [8, 5, 6, 9, 7], 'Science': [7, 9, 5, 4, 7], 'English': [7, 4, 7, 6, 8]}
a = df.sort_values(by='Science', ascending=0)
print('Sorting rows by Science:\n \n', a)
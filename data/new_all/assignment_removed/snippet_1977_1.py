import pandas as pd
data = {'Month': ['January', 'February', 'March', 'April'], 'Expense': [21525220.653, 31125840.875, 23135428.768, 56245263.942]}
dataframe = pd.DataFrame(data, columns=['Month', 'Expense'])
print('Given Dataframe :\n', dataframe)
print('\nResult :\n', dataframe)
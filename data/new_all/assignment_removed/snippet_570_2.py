import pandas as pd
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})
df1.combine_first(df2)
print('Original DataFrames:')
print(df1)
print('--------------------')
print(df2)
print('\nMerge two dataframes with different columns:')
result = df1.combine_first(df2)
print(result)
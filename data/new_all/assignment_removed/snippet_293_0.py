import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Original Orders DataFrame:')
print(df)
print('\\Result after group on salesman_id and apply different aggregate functions:')
df = df.groupby('salesman_id').agg(lambda x: x.sum() if x.name in ['sale_jan', 'sale_feb', 'sale_mar'] else x.mean())
print(df)
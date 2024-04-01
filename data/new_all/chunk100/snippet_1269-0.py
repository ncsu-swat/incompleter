import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002], 'sales_id': [5002, 5003, 5004, 5003, 5002, 5001, 5005, 5007, 5008, 5004, 5005, 5001]})
print('Original DataFrame:')
print(df)
groups = df.groupby(['customer_id', pd.cut(df.sales_id, 3)])
print(result)
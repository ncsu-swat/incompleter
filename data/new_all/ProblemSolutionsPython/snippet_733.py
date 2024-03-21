import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['7277 Surrey Ave.','920 N. Bishop Ave.','9910 Golden Star St.', '25 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)
def find_number(text):
    num = re.findall(r'[0-9]+',text)
    return " ".join(num)
df['number']=df['address'].apply(lambda x: find_number(x))
print("\Extracting numbers from dataframe columns:")
print(df)
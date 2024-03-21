import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({'name_email': ['Alberto Franco [email protected]', 'Gino Mcneill [email protected]', 'Ryan Parkes [email protected]', 'Eesha Hinton', 'Gino Mcneill [email protected]']})
print('Original DataFrame:')
print(df)

def find_email(text):
    return ','.join(email)
df['email'] = df['name_email'].apply(lambda x: find_email(x))
print('\\Extracting email from dataframe columns:')
print(df)
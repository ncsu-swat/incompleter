import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df.iloc[0, 2] = np.nan
df.iloc[3, 3] = np.nan
df.iloc[4, 1] = np.nan
df.iloc[9, 4] = np.nan
print('Original array:')
print(df)
print('\nBar charts in dataframe:')
df.style.bar(subset=['B', 'C'], color='#d65f5f')
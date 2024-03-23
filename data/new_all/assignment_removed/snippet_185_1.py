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

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color
print('\nNegative numbers red and positive numbers black:')
df.style.highlight_null(null_color='red')
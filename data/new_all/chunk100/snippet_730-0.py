import pandas as pd
series2 = pd.Series(list('pqrstuvwxy'))
print('Original Series:')
print(series1)
print(series2)
series1.append(series2)
df = pd.concat([series1, series2], axis=1)
print('\nStack two given series vertically and horizontally:')
print(df)
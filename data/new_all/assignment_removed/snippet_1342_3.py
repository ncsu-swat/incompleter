import pandas as pd
dtr = pd.date_range('2018-01-01', periods=12, freq='H')
print('Hourly frequency:')
print(dtr)
print('\nMinutely frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='S')
print('\nSecondly frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='2H')
print('nMultiple Hourly frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='5min')
print('\nMultiple Minutely frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='BQ')
print('\nMultiple Secondly frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='w')
print('\nWeekly frequency:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='2h20min')
print('\nCombine together day and intraday offsets-1:')
print(dtr)
dtr = pd.date_range('2018-01-01', periods=12, freq='1D10U')
print('\nCombine together day and intraday offsets-2:')
print(dtr)
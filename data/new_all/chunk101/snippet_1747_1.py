import pandas as pd
df1 = {'Name': ['George', 'Andrea', 'micheal', 'maggie', 'Ravi', 'Xien', 'Jalpa'], 'score1': [62, 47, 55, 74, 32, 77, 86], 'score2': [45, 78, 44, 89, 66, 49, 72]}
print('Given Dataframe :\n', df1)
df1['Score_diff'] = df1['score1'] - df1['score2']
print('\nDifference of score1 and score2 :\n', df1)
import pandas as pd
import numpy as np
import re

df = pd.read_csv('errs.tsv', sep='\t')

for col in df.columns[2:]:
    filename = col + '.txt'
    for line in open(filename, 'r').readlines():
        if 'snippet_' in line:
            line = line.strip()
            m = re.search('(\d+). (.*) \(snippet_(\d+).py.orig\)', line)
            if m is not None:
                err_msg = m.group(2)
                snippet_num = m.group(3)
                # print(snippet_num, ':', err_msg)
                df.loc[(df['snippet']==int(snippet_num)), [col]] = err_msg
            
# print(df.head())
# df.to_csv('errs.tsv', sep='\t', index=False)

groups = {x:0 for x in df.columns[2:]}
for i in range(len(df.columns)-1):
    for k in range(len(df)):
        if i > 0:
            if df.iloc[k][df.columns[i]] != df.iloc[k][df.columns[i+1]]:
                if str(df.iloc[k][df.columns[i]]) == "nan" and str(df.iloc[k][df.columns[i+1]]) == "nan":
                    pass
                else:
                    print(df.iloc[k][df.columns[i]], df.iloc[k][df.columns[i+1]])
                    groups[df.columns[i+1]] += 1

print(groups)

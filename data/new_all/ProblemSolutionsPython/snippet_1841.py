# import numpy and pandas module
import pandas as pd
import numpy as np


column=['a','b','c','d','e']
index=['A','B','C','D','E']


# create a dataframe of random values of array
df1 = pd.DataFrame(np.random.rand(5,5),
            columns=column, index=index)


print(df1)


print('\n\nDataframe after reindexing rows: \n',
df1.reindex(['B', 'D', 'A', 'C', 'E']))
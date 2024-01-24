#Source: https://stackoverflow.com/questions/58848474/value-counts-attributeerror-str-object-has-no-attribute-value-counts
class variableTreatment():
         def drop_zero_car_col(self, df):
            numerical = list(df._get_numeric_data().columns)
            categorical = list(set(df.columns).difference(set(numerical)))
            ls = []
            for i in categorical:
                d = dict(i.value_counts())
                if len(d)==1:
                    ls.append(i)
            df.drop(ls,axis=1,inplace=True)
            return(df)

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
df = pd.read_excel('CKD.xlsx')

VT = variableTreatment()

VT

VT.drop_zero_car_col(df).head()
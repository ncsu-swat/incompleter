#Source: https://stackoverflow.com/questions/68002673/how-to-resolve-an-attributeerror-can-only-use-str-accessor-with-string-values
import pandas as pd
import numpy as np 
from pandas import DataFrame as df 
import re


data = {'Tim': 'Tim@google.com', 'Rob': 'Rob@gmail.com', 'Jen': 'Jen@gmail.com', 'Wes': np.nan}

data = pd.Series(data)
    
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

matches = data.str.match(pattern, flags=re.IGNORECASE)

matches.str.get(1)
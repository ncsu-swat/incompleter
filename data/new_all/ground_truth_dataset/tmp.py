import pandas as pd
from datetime import datetime
import numpy as np
tmp_var0 = pd.date_range(start='1/1/2019', end='1/08/2019', freq='Min')
print('[FROM INNER-WORLD]')
print('VAR=range_date@6')
print('TYPE=' + type(tmp_var0).__name__)
range_date = tmp_var0
print(range_date)
import pandas as pd
import numpy as np
np.random.RandomState(100)
num_series = pd.Series(np.random.randint(1, 5, [15]))
print('Original Series:')
print(num_series)
print('Top 2 Freq:', num_series.value_counts())
print(num_series)
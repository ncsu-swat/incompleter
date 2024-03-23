import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
print('Original array:')
print(df)
print('\nDataframe - Gradient color:')
df.style.background_gradient(subset=['C'])
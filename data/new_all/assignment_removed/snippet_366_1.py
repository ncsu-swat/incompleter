import pandas as pd
import numpy as np
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
print('Original array:')
print(df)
print('\nDataframe - table style:')

def highlight_greaterthan(x):
    if x.C > 0.5:
        return ['background-color: yellow'] * 5
    else:
        return ['background-color: white'] * 5
df.style.apply(highlight_greaterthan, axis=1)
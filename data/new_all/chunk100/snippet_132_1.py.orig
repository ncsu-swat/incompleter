import pandas as pd
import numpy as np
import seaborn as sns
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
print('Original array:')
print(df)
print('\nDataframe - Heatmap style:')
cm = sns.light_palette('red', as_cmap=True)
df.style.background_gradient(cmap='viridis')
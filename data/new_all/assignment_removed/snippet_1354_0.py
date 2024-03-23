import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
plt.figure(figsize=(16, 10))
sns.heatmap(df.isnull(), cbar=False, cmap='YlGnBu')
plt.show()
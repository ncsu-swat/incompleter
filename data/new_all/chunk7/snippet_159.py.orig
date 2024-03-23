#Source: https://stackoverflow.com/questions/43523115/typeerror-ufunc-isnan-not-supported-for-the-input-types-seaborn-heatmap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_table(r"C:\Results.CST", sep='\s+',header=11, engine = 'python')
df2 = cridim[['Bottom','Location_X','Location_Y',]]  # Bottom , location X and Location  Y are my column labels
df3 = df2.pivot('Location_X','Location_Y','Bottom') # create pivot table for results

plt.figure(figsize=(15,15)) 
pivot_table = df3
plt.xlabel('X',size = 10) 
plt.ylabel('Y',size = 10) 
plt.title('btm CD',size = 10) 
sns.heatmap(pivot_table, annot=False, fmt=".1f", linewidths = 0.5, square = True, cmap = 'RdYlBu', vmin=2900, vmax = 3500) 
plt.show()
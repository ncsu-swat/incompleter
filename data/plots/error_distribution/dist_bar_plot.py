import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")

data = {
    'Error Type': ["TypeError", "FileNotFoundError", "ModuleNotFoundError", "NameError", "ValueError", "KeyError", "AttributeError"],
    'LexTP': [60, 20, 10, 10, 5, 3, 1],
    'IncTD': [31, 8, 1, 0, 11, 2, 7]

    # 'Error Type': ["TypeError", "ValueError", "NameError", "AttributeError", "FileNotFoundError", "ModuleNotFoundError", "KeyError", "Others"],
    # 'LexTP': [60, 5, 10, 1, 20, 10, 3],
    # 'IncTD': [31, 11, 0, 7, 8, 1, 2]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Error Type', var_name='Technique', value_name='Error Count')

plt.figure(figsize=(10, 4), dpi=150)
sns.barplot(data=df_melted, x='Error Type', y='Error Count', hue='Technique', palette='colorblind')

ax = plt.gca()
for label in ax.get_xticklabels():
    label.set_ha('right')
    
plt.xlabel('', fontsize=0)
plt.ylabel('Error Count', fontsize=18)
plt.xticks(fontsize=18, rotation=15)
plt.yticks(fontsize=18)
plt.legend(fontsize=24)

plt.tight_layout()
plt.savefig('lexecutor_all/residuals.pdf')
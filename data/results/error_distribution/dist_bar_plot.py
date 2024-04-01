import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")

data = {
    'Error Type': ["TypeError", "ValueError", "NameError", "AttributeError", "FileNotFoundError", "Others"],
    'Lexecutor': [60, 5, 10, 1, 20, 30],
    'Incompleter': [32, 12, 1, 8, 7, 20]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Error Type', var_name='Technique', value_name='Error Count')

plt.figure()
sns.barplot(data=df_melted, x='Error Type', y='Error Count', hue='Technique', palette='colorblind')

plt.xlabel('Error Types', fontsize=24)
plt.ylabel('Error Count', fontsize=24)
plt.xticks(fontsize=18, rotation=0)
plt.yticks(fontsize=18)
plt.legend(fontsize=24)
plt.show()
import os
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chunk_name = 'chunkall'
rules_per_snippet = []
for file in os.listdir('../../logs/incompleter/{}/logs'.format(chunk_name)):
    if file.startswith('snippet') and file.endswith('.json'):
        file_path = os.path.join('../../logs/incompleter/{}/logs'.format(chunk_name), file)
        with open(file_path, 'r') as snippet_log_file:
            snippet_log = json.load(snippet_log_file)
            counter = 0
            if 'iter' in snippet_log:
                for (iter, action_pattern) in snippet_log['iter'].items():
                    if action_pattern not in ['NoneType', 'Fixed', 'Unmocked']:
                        counter += 1
            if counter > 0:
                rules_per_snippet.append(counter)

# # Plot
# plt.figure(figsize=(10, 12), dpi=80)
# rules_per_snippet_plot = sns.boxplot(data=rules_per_snippet, palette='colorblind')

# # plt.xlabel('', fontsize=24)
# plt.ylabel('Rules applied per snippet', fontsize=24)
# plt.xticks(fontsize=0, rotation=0)
# plt.yticks(fontsize=18)
# # plt.legend(fontsize=24, loc='lower right')
# # plt.show()
# plt.savefig('dataset1_boxplot_rules_per_snippet', bbox_inches='tight')

# Plot
plt.figure(figsize=(12, 4), dpi=80)
bin_edges = np.arange(min(rules_per_snippet) - 0.5, max(rules_per_snippet) + 1.5, 1)
sns.histplot(data=rules_per_snippet, bins=bin_edges, kde=True, stat='percent')
plt.xlabel('Rules applied per snippet', fontsize=24)
plt.ylabel('% of snippets', fontsize=24)
plt.xticks(fontsize=18, rotation=0)
plt.yticks(fontsize=18)
plt.savefig('dataset2_hist_rules_per_snippet.pdf', bbox_inches='tight')





            
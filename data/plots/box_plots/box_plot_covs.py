import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

chunk = 'lexecutor_all'
data_path = '../../new_all/{}'.format(chunk)
lex_cov_path = '../../new_all/logs/lexecutor/{}/covs'.format(chunk)
inc_cov_path = '../../new_all/logs/incompleter/{}/covs'.format(chunk)

lex_covs, inc_covs = {}, {}
lex_stmt_covs, inc_stmt_covs = [], []
lex_br_covs, inc_br_covs = [], []

common_snippet_nos = []

for snippet_no in os.listdir(data_path):
    if snippet_no.startswith('snippet'):
        snippet_no = snippet_no.split('.')[0].split('_')[1]
        if os.path.exists(os.path.join(lex_cov_path, 'snippet_{}.json'.format(snippet_no))):
            if os.path.exists(os.path.join(inc_cov_path, 'snippet_{}.json'.format(snippet_no))):
                common_snippet_nos.append(snippet_no)

for snippet_no in common_snippet_nos:
    lex_cov = None
    with open(os.path.join(lex_cov_path, 'snippet_{}.json'.format(snippet_no)), 'r') as lex_cov_file, open(os.path.join(inc_cov_path, 'snippet_{}.json'.format(snippet_no)), 'r') as inc_cov_file:
        lex_cov = json.load(lex_cov_file)
        inc_cov = json.load(inc_cov_file)

        lex_stmt_covs.append(lex_cov['percent_covered'])
        inc_stmt_covs.append(inc_cov['percent_covered'])

        if lex_cov['num_branches'] > 0 and inc_cov['num_branches'] > 0:
            lex_br_covs.append((lex_cov['covered_branches']/lex_cov['num_branches'])*100)
            inc_br_covs.append((inc_cov['covered_branches']/inc_cov['num_branches'])*100)

# Build DataFrames
df_covs = pd.DataFrame({
    'metrics': ['statement']*len(lex_stmt_covs) + ['branch']*len(lex_br_covs),
    'Lexecutor': lex_stmt_covs + lex_br_covs,
    'Incompleter': inc_stmt_covs + inc_br_covs
})
df_covs_melted = pd.melt(df_covs, id_vars='metrics', var_name='technique', value_name='covs')

# Plot
fig, axes = plt.subplots(1, 1, figsize=(12, 6))
stmt_br = sns.boxplot(data=df_covs_melted, x='metrics', y='covs', hue='technique', palette='colorblind', ax=axes)

# plt.xlabel('Dataset 2', fontsize=24)
# plt.ylabel('Coverage (%)', fontsize=24)
# plt.xticks(fontsize=18, rotation=0)
# plt.yticks(fontsize=18)
# plt.legend(fontsize=24, loc='lower right')
# plt.show()

from scipy import stats
res = stats.shapiro(lex_stmt_covs)
print(res.pvalue)
res = stats.shapiro(inc_stmt_covs)
print(res.pvalue)
res = stats.shapiro(lex_br_covs)
print(res.pvalue)
res = stats.shapiro(inc_br_covs)
print(res.pvalue)


from scipy.stats import mannwhitneyu
U1, p = mannwhitneyu(lex_stmt_covs, inc_stmt_covs)
print(p)
U1, p = mannwhitneyu(lex_br_covs, inc_br_covs)
print(p)

from cliffs_delta import cliffs_delta
d, res = cliffs_delta(inc_stmt_covs, lex_stmt_covs)
print(d, res)
d, res = cliffs_delta(inc_br_covs, lex_br_covs)
print(d, res)
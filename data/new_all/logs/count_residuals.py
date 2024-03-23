import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})
fig, axs = plt.subplots(1)

inc_residual_errors = ['TypeError', 'ValueError', 'AttributeError', 'FileNotFoundError', 'IndexError', 'KeyError', 'Others']
inc_residual_counts = [33, 11, 9, 7, 3, 2, 13]

lex_residual_errors = ['TypeError', 'FileNotFoundError', 'NameError', 'ValueError', 'IndexError', 'KeyError', 'Others']
lex_residual_counts = [57, 19, 9, 4, 4, 3, 17]

axs.tick_params(axis='x', rotation=15)
axs.set_ylabel('Error Count')
axs.bar(lex_residual_errors, lex_residual_counts)

plt.show()
import os
import pickle
import matplotlib.pyplot as plt

lasterrs_counter = {}
with open('chunk1/lasterrs.pkl', 'rb') as last_err_pkl:
    lasterrs = pickle.load(last_err_pkl)

    for err in lasterrs:
        if err not in lasterrs_counter.keys():
            lasterrs_counter[err] = 1
        else:
            lasterrs_counter[err] += 1

with open('chunk6/lasterrs.pkl', 'rb') as last_err_pkl:
    lasterrs = pickle.load(last_err_pkl)

    for err in lasterrs:
        if err not in lasterrs_counter.keys():
            lasterrs_counter[err] = 1
        else:
            lasterrs_counter[err] += 1

sorted_lasterrs_counter = dict(sorted(lasterrs_counter.items(), key=lambda item: item[1]))
# print(sorted_lasterrs_counter)

# First Counter
first_counter = {}
for file in os.listdir('../../StackoverflowData-master/snippets'):
    err_type = file.split('-')[-1].split('.')[0]
    if err_type not in first_counter:
        first_counter[err_type] = 1
    else:
        first_counter[err_type] += 1
sorted_first_counter = dict(sorted(first_counter.items(), key=lambda item: item[1]))
total_first_counter = 0
for key, item in sorted_first_counter.items():
    total_first_counter += item
for key, item in sorted_first_counter.items():
    sorted_first_counter[key] = item/total_first_counter

incompleter = {
    'NameError': 0.009,
    'OSError': 0.01,
    'SyntaxError': 0.012,
    'IndexError': 0.015,
    'ModuleNotFoundError': 0.027,
    'ValueError': 0.04,
    'FileNotFoundError': 0.07,
    'KeyError': 0.078,
    'ImportError': 0.085,
    'AttributeError': 0.195,
    'TypeError': 0.46
}
lexecutor = {
    'OSError': 0.0034, 'ModuleNotFoundError': 0.0034, 'RuntimeError': 0.0046, 'TclError': 0.0069, 'ValueError': 0.0069, 'SSLCertVerificationError': 0.0069, 'IndexError': 0.019, 'AttributeError': 0.039, 'KeyError': 0.048, 'NameError': 0.072, 'FileNotFoundError': 0.1712, 'TypeError': 0.615
}

plt.title('LExecutor Final Error Distribution')
plt.xticks(rotation=10)
plt.bar(lexecutor.keys(), lexecutor.values(), width=0.4)
plt.show()

    
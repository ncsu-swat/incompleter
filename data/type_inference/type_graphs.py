import json
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import os

with open('./data/type_inference/snippets_info_incompleter_317.json', 'r') as file:
    snippets_info_incompleter = json.load(file)

lexecutor_predictions = Counter()
incompleter_predictions = Counter()

for snippet in snippets_info_incompleter:
    for identifier in snippet['identifiers'].values():
        lexecutor_type = identifier['lexecutor_predicted_type']
        incompleter_type = identifier['incompleter_predicted_type']
        
        if lexecutor_type not in ["todo", "did not implement"] and incompleter_type not in ["todo", "did not implement"]:
            lexecutor_predictions[lexecutor_type] += 1
            incompleter_predictions[incompleter_type] += 1

        # if lexecutor_type not in ["todo", "did not implement"]:
        #     lexecutor_predictions[lexecutor_type] += 1

        # if incompleter_type not in ["todo", "did not implement"]:
        #     incompleter_predictions[incompleter_type] += 1

total_lexecutor = sum(lexecutor_predictions.values())
total_incompleter = sum(incompleter_predictions.values())

# Prints the counts and percentages for each type
lexecutor_output = "LExecutor Predicted Types and Percentages: "
lexecutor_output += ", ".join([f"{type}: ({count/total_lexecutor*100:.2f}%)" for type, count in lexecutor_predictions.most_common()])

incompleter_output = "Incompleter Predicted Types and Percentages: "
incompleter_output += ", ".join([f"{type}: ({count/total_incompleter*100:.2f}%)" for type, count in incompleter_predictions.most_common()])

print(lexecutor_output)
print("\n")
print(incompleter_output)

def plot_histogram(predictions, title):
    sorted_predictions = dict(sorted(predictions.items(), key=lambda item: (-item[1], item[0])))
    total_count = sum(predictions.values())
    percentages = [(count / total_count * 100) for count in sorted_predictions.values()]
    labels = list(sorted_predictions.keys())
    plt.figure(figsize=(10, 6))
    indexes = np.arange(len(labels))
    plt.bar(indexes, percentages, color='skyblue', edgecolor='black')
    plt.xlabel('Predicted Types', fontsize=12)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.xticks(indexes, labels, rotation=45, ha="right")
    plt.title(title, fontsize=14)
    plt.tight_layout()
    plt.show()


plot_histogram(lexecutor_predictions, 'LExecutor Predicted Types')
plot_histogram(incompleter_predictions, 'Incompleter Predicted Types')

from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles

dataset1 = {
    'only_inc': 0.25,
    'only_lex': 0.12,
    'both': 0.42
}
dataset2 = {
    'only_inc': 0.23,
    'only_lex': 0.13,
    'both': 0.31
}

def draw(dataset):
    # Create a weighted Venn diagram
    venn_diagram = venn2(subsets=(dataset['only_inc'], dataset['only_lex'], dataset['both']), set_labels=('Set 1', 'Set 2'))
    circles = venn2_circles(subsets=(dataset['only_inc'], dataset['only_lex'], dataset['both']), linewidth=2)
    return venn_diagram, circles

venn_diagram, circles = draw(dataset1)

# Increase font size of labels
for (idx, text) in enumerate(venn_diagram.set_labels):
    if idx==0:
        text.set_text('Incompleter')
        text.set_x(text.get_position()[0]-0.05)
    elif idx==1:
        text.set_text('Lexecutor')
        text.set_x(text.get_position()[0]+0.05)
    
    text.set_fontsize(28)
    text.set_fontweight('bold')
    text.set_y(-0.57)

for label in venn_diagram.subset_labels:
    label.set_fontsize(38)
    # label.set_fontweight('bold')

# Show plot
plt.show()

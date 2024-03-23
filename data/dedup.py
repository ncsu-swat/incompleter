import os

snippets1 = []
snippets2 = []

names1 = []
names2 = []

dups = {}

for file in os.listdir('data/new_all/chunk5'):
    if file.endswith(".py.orig"):
        with open(os.path.join('data/new_all/chunk5', file), 'r') as _file:
            snippets1.append(_file.read())
            names1.append(file)
for file in os.listdir('data/new_all/chunk6'):
    if file.endswith(".py.orig"):
        with open(os.path.join('data/new_all/chunk6', file), 'r') as _file:
            snippets2.append(_file.read())
            names2.append(file)

for i in range(len(snippets1)):
    for j in range(len(snippets2)):
        if snippets1[i] == snippets2[j]:
            try:
                path = os.path.join('data/new_all/chunk6', names2[j])
                print(path)
                os.remove(path)
                print(names1[i], ', ', names2[j])
            except Exception as e:
                pass
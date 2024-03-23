fname = input('Enter file name: ')
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print('Number of lines:')
print(num_lines)
import sys
arr = []
freq = []
max = -sys.maxsize - 1
print('Enter the Element of the array:')
for i in range(0, size):
    num = int(input())
    arr.append(num)
for i in range(0, size):
    if arr[i] >= max:
        max = arr[i]
for i in range(0, max + 1):
    freq.append(0)
for i in range(0, size):
    freq[arr[i]] += 1
for i in range(0, max + 1):
    if freq[i] != 0:
        print('occurs ', i, ' ', freq[i], ' times')
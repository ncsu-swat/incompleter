str = input('Enter the String:')
arr = [0] * 256
for i in range(len(str)):
    if str[i] == ' ':
        continue
    arr[num] += 1
print('Frequency of character in a string are:')
for i in range(256):
    if arr[i] != 0:
        print(chr(i), ' occurs ', arr[i], ' times')
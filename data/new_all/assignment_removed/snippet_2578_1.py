size = int(input('Enter the size of the array: '))
print('Enter the Element of the array:')
for i in range(0, size):
    num = int(input())
    arr.append(num)
print('Before sorting array elements are:')
for i in range(0, size):
    print(arr[i], end=' ')
for i in range(0, size):
    for j in range(i + 1, size):
        if arr[i] >= arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print('\nAfter sorting array elements are:')
for i in range(0, size):
    print(arr[i], end=' ')
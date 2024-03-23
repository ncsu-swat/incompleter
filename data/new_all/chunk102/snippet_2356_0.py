import math
col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
trace = 0
sum = 0
for i in range(0, row_size):
    for j in range(0, col_size):
        if i == j:
            trace += matrix[i][j]
        sum += matrix[i][j]
normal = math.sqrt(sum)
print('Normal Of the Matrix is: ', normal)
print('Trace Of the Matrix is: ', trace)
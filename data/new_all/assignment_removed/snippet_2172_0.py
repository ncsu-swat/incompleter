import sys
col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
min = sys.maxsize
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] <= min:
            min = matrix[i][j]
print('The Minimum element of the Given 2d array is: ', min)
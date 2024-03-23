col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j:
            sum += matrix[i][j]
print('Sum of diagonals Element is: ', sum)
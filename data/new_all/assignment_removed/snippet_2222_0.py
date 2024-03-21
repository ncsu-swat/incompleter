col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
matrix1 = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix1.append([int(j) for j in input().split()])
sub_matrix = [[0 for i in range(col_size)] for i in range(row_size)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        sub_matrix[i][j] = matrix[i][j] - matrix1[i][j]
print('Subtraction of the two Matrices is:')
for m in sub_matrix:
    print(m)
col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
matrix1 = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix1.append([int(j) for j in input().split()])
sum = 0
mul_matrix = [[0 for i in range(col_size)] for i in range(row_size)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        for k in range(row_size):
            sum += matrix[i][j] * matrix1[i][j]
        mul_matrix[i][j] = sum
print('Multiplication of the two Matrices is:')
for m in mul_matrix:
    print(m)
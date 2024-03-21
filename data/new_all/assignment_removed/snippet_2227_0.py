col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
if row_size != col_size:
    print('Given Matrix is not a Square Matrix.')
else:
    tran_matrix = [[0 for i in range(col_size)] for i in range(row_size)]
    for i in range(0, row_size):
        for j in range(0, col_size):
            tran_matrix[i][j] = matrix[j][i]
flag = 0
for i in range(0, row_size):
    for j in range(0, col_size):
        if matrix[i][j] != tran_matrix[i][j]:
            flag = 1
            break
if flag == 1:
    print('Given Matrix is not a symmetric Matrix.')
else:
    print('Given Matrix is a symmetric Matrix.')
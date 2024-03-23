col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
count_zero = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            count_zero += 1
if count_zero > row_size * col_size // 2:
    print('Given Matrix is a sparse Matrix.')
else:
    print('Given Matrix is not a sparse Matrix.')
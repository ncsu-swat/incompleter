col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
point = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j and matrix[i][j] != 1:
            point = 1
            break
        elif i != j and matrix[i][j] != 0:
            point = 1
            break
if point == 1:
    print('Given Matrix is not an identity matrix.')
else:
    print('Given Matrix is an identity matrix.')
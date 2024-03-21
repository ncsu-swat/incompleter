col_size = int(input('Enter the columns Size Of the Matrix:'))
matrix = []
print('Enter the Matrix Element:')
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])
sum = 0
for i in range(0, row_size):
    for j in range(0, col_size):
        sum += matrix[i][j]
print('Sum of the Given Matrix Elements is: ', sum)
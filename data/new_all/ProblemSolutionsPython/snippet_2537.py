# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the 1st matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

# check except Diagonal all elements are 0 or not
# and check all diagonal elements are same or not
point=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i!=j and matrix[i][j]!=0:
            point=1
            break
        if i==j and matrix[i][j]!=matrix[i][j]:
            point = 1
            break

if point==1:
    print("Given Matrix is not a Scaler Matrix.")
else:
    print("Given Matrix is a Scaler Matrix.")
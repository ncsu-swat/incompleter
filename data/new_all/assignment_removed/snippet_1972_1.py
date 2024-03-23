import numpy

def colsum(arr, n, m):
    for i in range(n):
        for j in range(m):
            su += arr[j][i]
        print(su, end=' ')
TwoDList = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
TwoDArray = numpy.array(TwoDList)
print('2D Array:')
print(TwoDArray)
print('\nColumn-wise Sum:')
colsum(TwoDArray, len(TwoDArray[0]), len(TwoDArray))
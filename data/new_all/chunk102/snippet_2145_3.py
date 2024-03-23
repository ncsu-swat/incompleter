def maximumAdjacent(arr1, n):
    arr2 = []
    for i in range(1, n):
        r = max(arr1[i], arr1[i - 1])
        arr2.append(r)
    for ele in arr2:
        print(ele, end=' ')
if __name__ == '__main__':
    n = 6
    maximumAdjacent(arr1, n)
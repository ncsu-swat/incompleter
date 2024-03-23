def interSection(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print('Intersection : ', result)
if __name__ == '__main__':
    arr2 = [2, 3, 5, 6]
    interSection(arr1, arr2)
def interSection(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print('Intersection : ', result)
if __name__ == '__main__':
    arr1 = [1, 3, 4, 5, 7]
    interSection(arr1, arr2)
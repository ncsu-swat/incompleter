def IntersecOfSets(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)
    print(final_list)
if __name__ == '__main__':
    arr1 = [1, 5, 10, 20, 40, 80, 100]
    arr2 = [6, 7, 20, 80, 100]
    IntersecOfSets(arr1, arr2, arr3)
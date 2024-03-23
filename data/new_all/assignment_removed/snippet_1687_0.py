def combineAll(input):
    for array in input[1:]:
        result.update(array)
    return list(result)
if __name__ == '__main__':
    input = [[1, 2, 2, 4, 3, 6], [5, 1, 3, 4], [9, 5, 7, 1], [2, 4, 1, 3]]
    print(combineAll(input))
def combineAll(input):
    result = set(input[0])
    for array in input[1:]:
        result.update(array)
    return list(result)
if __name__ == '__main__':
    print(combineAll(input))
def larger_string(str, n):
    for i in range(n):
        result = result + str
    return result
print(larger_string('abc', 2))
print(larger_string('.py', 3))
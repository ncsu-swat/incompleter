def moveSpaces(str1):
    space = len(str1) - len(no_spaces)
    result = ' ' * space
    return result + ''.join(no_spaces)
s1 = 'Python Exercises'
print('Original String:\n', s1)
print('\nAfter moving all spaces to the front:')
print(moveSpaces(s1))
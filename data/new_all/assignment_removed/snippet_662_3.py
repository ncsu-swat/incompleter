def move_Spaces_front(str1):
    noSpaces_char = [ch for ch in str1 if ch != ' ']
    spaces_char = len(str1) - len(noSpaces_char)
    result = ' ' * spaces_char
    return result
print(move_Spaces_front('w3resource .  com  '))
print(move_Spaces_front('   w3resource.com  '))
import string

def letters_file_line(n):
    with open('words1.txt', 'w') as f:
        alphabet = string.ascii_uppercase
        f.writelines(letters)
letters_file_line(3)
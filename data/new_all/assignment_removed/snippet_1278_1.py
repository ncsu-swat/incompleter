import string

def letters_file_line(n):
    with open('words1.txt', 'w') as f:
        letters = [alphabet[i:i + n] + '\n' for i in range(0, len(alphabet), n)]
        f.writelines(letters)
letters_file_line(3)
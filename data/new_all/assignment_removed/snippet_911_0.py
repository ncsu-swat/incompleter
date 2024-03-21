def duplicate_letters(text):
    word_list = text.split()
    for word in word_list:
        if len(word) > len(set(word)):
            return False
    return True
print('Original text:')
print(text)
print('Check whether any word in the said sting contains duplicate characrters or not!')
print(duplicate_letters(text))
text = 'Python Exercise.'
print('\nOriginal text:')
print(text)
print('Check whether any word in the said sting contains duplicate characrters or not!')
print(duplicate_letters(text))
text = 'The wait is over.'
print('\nOriginal text:')
print(text)
print('Check whether any word in the said sting contains duplicate characrters or not!')
print(duplicate_letters(text))
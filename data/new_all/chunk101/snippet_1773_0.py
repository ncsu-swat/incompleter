def printWords(s):
    for word in s:
        if len(word) % 2 == 0:
            print(word)
s = 'i am muskan'
printWords(s)
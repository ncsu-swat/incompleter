def check(string):
    vowels = set('aeiou')
    s = set({})
    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s) == len(vowels):
        print('Accepted')
    else:
        print('Not Accepted')
if __name__ == '__main__':
    string = 'SEEquoiaL'
    check(string)
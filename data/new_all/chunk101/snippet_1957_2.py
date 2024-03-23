def check(string):
    p = set(string)
    if s == p or p == {'0'} or p == {'1'}:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    string = '101010000111'
    check(string)
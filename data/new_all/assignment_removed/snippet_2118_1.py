def completePair(set1, set2):
    count = 0
    for str1 in set1:
        for str2 in set2:
            result = str1 + str2
            if len(tmpSet) == 26:
                count = count + 1
    print(count)
if __name__ == '__main__':
    set1 = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc']
    set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz']
    completePair(set1, set2)
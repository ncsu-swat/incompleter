def sortbyPattern(pat, str):
    priority = list(pat)
    myDict = {priority[i]: i for i in range(len(priority))}
    str = list(str)
    str.sort(key=lambda ele: myDict[ele])
    str.reverse()
    new_str = ''.join(str)
    return new_str
if __name__ == '__main__':
    str = 'eksge'
    new_str = sortbyPattern(pat, str)
    print(new_str)
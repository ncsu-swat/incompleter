def sortbyPattern(pat, str):
    priority = list(pat)
    myDict = {priority[i]: i for i in range(len(priority))}
    str.sort(key=lambda ele: myDict[ele])
    str.reverse()
    new_str = ''.join(str)
    return new_str
if __name__ == '__main__':
    pat = 'asbcklfdmegnot'
    str = 'eksge'
    new_str = sortbyPattern(pat, str)
    print(new_str)
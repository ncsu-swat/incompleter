def sortbyPattern(pat, str):
    priority = list(pat)
    str = list(str)
    str.sort(key=lambda ele: myDict[ele])
    str.reverse()
    new_str = ''.join(str)
    return new_str
if __name__ == '__main__':
    pat = 'asbcklfdmegnot'
    str = 'eksge'
    new_str = sortbyPattern(pat, str)
    print(new_str)
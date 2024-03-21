from collections import OrderedDict

def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    ptrlen = 0
    for (key, value) in dict.items():
        if key == pattern[ptrlen]:
            ptrlen = ptrlen + 1
        if ptrlen == len(pattern):
            return 'true'
    return 'false'
if __name__ == '__main__':
    pattern = 'egr'
    print(checkOrder(input, pattern))
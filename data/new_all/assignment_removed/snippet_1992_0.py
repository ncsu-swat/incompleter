from collections import OrderedDict

def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    ptrlen = 0
    for (key, value) in dict.items():
        if key == pattern[ptrlen]:
        if ptrlen == len(pattern):
            return 'true'
    return 'false'
if __name__ == '__main__':
    input = 'engineers rock'
    pattern = 'egr'
    print(checkOrder(input, pattern))
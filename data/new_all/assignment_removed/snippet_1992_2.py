from collections import OrderedDict

def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    for (key, value) in dict.items():
        if key == pattern[ptrlen]:
            ptrlen = ptrlen + 1
        if ptrlen == len(pattern):
            return 'true'
    return 'false'
if __name__ == '__main__':
    input = 'engineers rock'
    pattern = 'egr'
    print(checkOrder(input, pattern))
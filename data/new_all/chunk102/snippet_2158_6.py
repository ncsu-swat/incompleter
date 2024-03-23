from collections import Counter

def commonElement(ar1, ar2, ar3):
    ar1 = Counter(ar1)
    ar2 = Counter(ar2)
    ar3 = Counter(ar3)
    resultDict = dict(ar1.items() & ar2.items() & ar3.items())
    common = []
    for (key, val) in resultDict.items():
        for i in range(0, val):
            common.append(key)
    print(common)
if __name__ == '__main__':
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    commonElement(ar1, ar2, ar3)
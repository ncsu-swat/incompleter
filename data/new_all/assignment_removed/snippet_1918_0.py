from collections import Counter

def minSubsets(input):
    freqDict = Counter(input)
    print(max(freqDict.values()))
if __name__ == '__main__':
    minSubsets(input)
from collections import Counter

def maxAnagramSize(input):
    input = input.split(' ')
    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))
    print(max(freqDict.values()))
if __name__ == '__main__':
    input = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input)
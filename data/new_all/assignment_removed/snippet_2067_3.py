from collections import Counter

def winner(input):
    votes = Counter(input)
    dict = {}
    for value in votes.values():
        dict[value] = []
    for (key, value) in votes.items():
        dict[value].append(key)
    if len(dict[maxVote]) > 1:
        print(sorted(dict[maxVote])[0])
    else:
        print(dict[maxVote][0])
if __name__ == '__main__':
    input = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
    winner(input)
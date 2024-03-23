def word_count(str):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count('the quick brown fox jumps over the lazy dog.'))
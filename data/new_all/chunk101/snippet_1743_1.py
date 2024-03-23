from difflib import get_close_matches

def closeMatches(patterns, word):
    print(get_close_matches(word, patterns))
if __name__ == '__main__':
    patterns = ['ape', 'apple', 'peach', 'puppy']
    closeMatches(patterns, word)
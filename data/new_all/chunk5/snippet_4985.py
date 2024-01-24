# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31988132/list-of-words-typeerror-str-does-not-support-the-buffer-interface
# Hangman
#
# -----------------------------------
# Helper code
# List of words - TypeError: 'str' does not support the buffer interface, Python v.3.4


from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(666113)

except ImportError:
    pass
try:
    import string
    _l_(666115)

except ImportError:
    pass

WORDLIST_FILENAME = "words.txt"
_l_(666116)

def load_words():
    _l_(666141)

    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    _c_(666118, _n_(666117, "print", lambda: print), "Loading word list from file...")
    _l_(666119)
    # inFile: file
    inFile = _c_(666122, _n_(666120, "open", lambda: open), _n_(666121, "WORDLIST_FILENAME", lambda: WORDLIST_FILENAME), 'r', 0)
    _l_(666123)
    # line: string
    line = _c_(666126, _a_(666125, _n_(666124, "inFile", lambda: inFile), "readline"))
    _l_(666127)
    # wordlist: list of strings
    wordlist = _c_(666131, _a_(666129, _n_(666128, "str", lambda: str), "split"), _n_(666130, "line", lambda: line))
    _l_(666132)
    _c_(666137, _n_(666133, "print", lambda: print), "  ", _c_(666136, _n_(666134, "len", lambda: len), _n_(666135, "wordlist", lambda: wordlist)), "words loaded.")
    _l_(666138)
    aux = _n_(666139, "wordlist", lambda: wordlist)
    _l_(666140)
    return aux

def choose_word(wordlist):
    _l_(666147)

    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    aux = _c_(666145, _a_(666143, _n_(666142, "random", lambda: random), "choice"), _n_(666144, "wordlist", lambda: wordlist))
    _l_(666146)
    return aux

# end of helper code
# -----------------------------------

wordlist = _c_(666149, _n_(666148, "load_words", lambda: load_words))
_l_(666150)
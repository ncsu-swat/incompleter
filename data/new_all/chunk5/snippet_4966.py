# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37003943/previous-function-does-not-carry-over-to-next-function-nameerror-name-is-not-de
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(665382)

except ImportError:
    pass

def setup():
    _l_(665392)


    _c_(665384, _n_(665383, "print", lambda: print), "Reading Word List...")
    _l_(665385)
    _c_(665387, _n_(665386, "print", lambda: print), "Selecting Secret Word...")
    _l_(665388)
    _c_(665390, _n_(665389, "print", lambda: print), "A secret word has been selected...")
    _l_(665391)

_c_(665394, _n_(665393, "setup", lambda: setup))
_l_(665395)

def loadwordlist():
    _l_(665422)


    word = _c_(665401, _a_(665400, _c_(665399, _a_(665398, _c_(665397, _n_(665396, "open", lambda: open), 'words.txt'), "read")), "splitlines"))
    _l_(665402)
    secret_word = _c_(665408, _a_(665407, _c_(665406, _a_(665404, _n_(665403, "random", lambda: random), "choice"), _n_(665405, "word", lambda: word)), "lower"))
    _l_(665409)
    guessed_word = []
    _l_(665410)
    guessed_letters = []
    _l_(665411)
    for letters in _n_(665412, "secret_word", lambda: secret_word):
        _l_(665417)

        _c_(665415, _a_(665414, _n_(665413, "guessed_word", lambda: guessed_word), "append"), '_')
        _l_(665416)
    aux = _c_(665420, _a_(665418, ' ', "join"), _n_(665419, "guessed_word", lambda: guessed_word))
    _l_(665421)
    return aux

_c_(665426, _n_(665423, "print", lambda: print), _c_(665425, _n_(665424, "loadwordlist", lambda: loadwordlist)))
_l_(665427)

total_guesses = 10
_l_(665428)
_c_(665433, _n_(665429, "print", lambda: print), _c_(665432, _a_(665430, ("You have {} guesses left"), "format"), _n_(665431, "total_guesses", lambda: total_guesses)))
_l_(665434)

def gethint():
    _l_(665456)


    _c_(665436, _n_(665435, "loadwordlist", lambda: loadwordlist))
    _l_(665437)
    guess = _c_(665439, _n_(665438, "input", lambda: input), "Please enter a guess:")
    _l_(665440)
    guess = _c_(665443, _a_(665442, _n_(665441, "guess", lambda: guess), "lower"))
    _l_(665444)
    if _n_(665445, "guess", lambda: guess) in _n_(665446, "guessed_word", lambda: guessed_word):
        _l_(665455)

        _c_(665448, _n_(665447, "print", lambda: print), "You guessed Correctly")
        _l_(665449)
        _c_(665453, _a_(665451, _n_(665450, "guessed_letters", lambda: guessed_letters), "append"), _n_(665452, "guess", lambda: guess))
        _l_(665454)

_c_(665458, _n_(665457, "gethint", lambda: gethint))
_l_(665459)
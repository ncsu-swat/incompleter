# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37003943/previous-function-does-not-carry-over-to-next-function-nameerror-name-is-not-de
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(680000)

except ImportError:
    pass

def setup():
    _l_(680010)


    _c_(680002, _n_(680001, "print", lambda: print), "Reading Word List...")
    _l_(680003)
    _c_(680005, _n_(680004, "print", lambda: print), "Selecting Secret Word...")
    _l_(680006)
    _c_(680008, _n_(680007, "print", lambda: print), "A secret word has been selected...")
    _l_(680009)

_c_(680012, _n_(680011, "setup", lambda: setup))
_l_(680013)

def loadwordlist():
    _l_(680040)


    word = _c_(680019, _a_(680018, _c_(680017, _a_(680016, _c_(680015, _n_(680014, "open", lambda: open), 'words.txt'), "read")), "splitlines"))
    _l_(680020)
    secret_word = _c_(680026, _a_(680025, _c_(680024, _a_(680022, _n_(680021, "random", lambda: random), "choice"), _n_(680023, "word", lambda: word)), "lower"))
    _l_(680027)
    guessed_word = []
    _l_(680028)
    guessed_letters = []
    _l_(680029)
    for letters in _n_(680030, "secret_word", lambda: secret_word):
        _l_(680035)

        _c_(680033, _a_(680032, _n_(680031, "guessed_word", lambda: guessed_word), "append"), '_')
        _l_(680034)
    aux = _c_(680038, _a_(680036, ' ', "join"), _n_(680037, "guessed_word", lambda: guessed_word))
    _l_(680039)
    return aux

_c_(680044, _n_(680041, "print", lambda: print), _c_(680043, _n_(680042, "loadwordlist", lambda: loadwordlist)))
_l_(680045)

total_guesses = 10
_l_(680046)
_c_(680051, _n_(680047, "print", lambda: print), _c_(680050, _a_(680048, ("You have {} guesses left"), "format"), _n_(680049, "total_guesses", lambda: total_guesses)))
_l_(680052)

def gethint():
    _l_(680074)


    _c_(680054, _n_(680053, "loadwordlist", lambda: loadwordlist))
    _l_(680055)
    guess = _c_(680057, _n_(680056, "input", lambda: input), "Please enter a guess:")
    _l_(680058)
    guess = _c_(680061, _a_(680060, _n_(680059, "guess", lambda: guess), "lower"))
    _l_(680062)
    if _n_(680063, "guess", lambda: guess) in _n_(680064, "guessed_word", lambda: guessed_word):
        _l_(680073)

        _c_(680066, _n_(680065, "print", lambda: print), "You guessed Correctly")
        _l_(680067)
        _c_(680071, _a_(680069, _n_(680068, "guessed_letters", lambda: guessed_letters), "append"), _n_(680070, "guess", lambda: guess))
        _l_(680072)

_c_(680076, _n_(680075, "gethint", lambda: gethint))
_l_(680077)
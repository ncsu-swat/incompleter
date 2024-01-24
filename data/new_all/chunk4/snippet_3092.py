# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47373427/typeerror-function-object-is-not-subscriptable-on-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(606047)

except ImportError:
    pass

def num():
    _l_(606060)

    """Returns a number between 1000 and 9999."""
    num = _c_(606052, _n_(606048, "str", lambda: str), _c_(606051, _a_(606050, _n_(606049, "random", lambda: random), "randint"), 1000, 9999))
    _l_(606053)
    _c_(606056, _n_(606054, "print", lambda: print), "Random number is: " + _n_(606055, "num", lambda: num)) #for testing purposes
    _l_(606057) #for testing purposes
    aux = _n_(606058, "num", lambda: num)
    _l_(606059)
    return aux

def userNum():
    _l_(606088)

    """Asks user for a number between 1000 and 9999."""
    while True:
        _l_(606081)

        try:
            _l_(606072)

            userNum = _c_(606064, _n_(606061, "int", lambda: int), _c_(606063, _n_(606062, "input", lambda: input), "Choose a number between 1000 and 9999: "))
            _l_(606065)
        except _n_(606066, "ValueError", lambda: ValueError):
            _l_(606071)

            _c_(606068, _n_(606067, "print", lambda: print), "This isn't a number, try again.")
            _l_(606069)
            continue
            _l_(606070)
        if _n_(606073, "userNum", lambda: userNum) < 1000 or _n_(606074, "userNum", lambda: userNum) > 9990:
            _l_(606080)

            _c_(606076, _n_(606075, "print", lambda: print), "Your number isn't between 1000 and 9999, try again.")
            _l_(606077)
            continue
            _l_(606078)
        else:
            break
            _l_(606079)
    userNum = _c_(606084, _n_(606082, "str", lambda: str), _n_(606083, "userNum", lambda: userNum))
    _l_(606085)
    aux = _n_(606086, "userNum", lambda: userNum)
    _l_(606087)
    return aux

def numCheck(num, userNum):
    _l_(606112)

    """Checks the number of cows and bulls."""
    cow = 0
    _l_(606089)
    bull = 0
    _l_(606090)
    for i in _c_(606092, _n_(606091, "range", lambda: range), 0, 3):
        _l_(606100)

        if _n_(606093, "userNum", lambda: userNum)[_n_(606094, "i", lambda: i)] == _n_(606095, "num", lambda: num)[_n_(606096, "i", lambda: i)]:
            _l_(606099)

            cow += 1
            _l_(606097)
        else:
            bull += 1
            _l_(606098)
    _c_(606108, _n_(606101, "print", lambda: print), "You have " + _c_(606104, _n_(606102, "str", lambda: str), _n_(606103, "cow", lambda: cow)) + " cow(s) and you have " + _c_(606107, _n_(606105, "str", lambda: str), _n_(606106, "bull", lambda: bull)) + " bull(s).")
    _l_(606109)
    aux = _n_(606110, "cow", lambda: cow)
    _l_(606111)
    return aux

def gameLoop():
    _l_(606130)

    """Loops the game until the user find the right number."""
    _c_(606114, _n_(606113, "num", lambda: num))
    _l_(606115)
    cow = 0
    _l_(606116)
    if _n_(606117, "cow", lambda: cow) < 4:
        _l_(606129)

        _c_(606119, _n_(606118, "userNum", lambda: userNum))
        _l_(606120)
        _c_(606124, _n_(606121, "numCheck", lambda: numCheck), _n_(606122, "num", lambda: num), _n_(606123, "userNum", lambda: userNum))
        _l_(606125)
    else:
        _c_(606127, _n_(606126, "print", lambda: print), "Congratulation, You found the right number!")
        _l_(606128)

_c_(606132, _n_(606131, "gameLoop", lambda: gameLoop))
_l_(606133)
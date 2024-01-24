# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72299517/typeerror-in-python-in-custom-input-function-exception-handling
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(350938)

except ImportError:
    pass
randInt = _c_(350941, _a_(350940, _n_(350939, "random", lambda: random), "randint"), 1, 100)
_l_(350942)
count = 1
_l_(350943)
_c_(350948, _n_(350944, "print", lambda: print), "RandInt: " + _c_(350947, _n_(350945, "str", lambda: str), _n_(350946, "randInt", lambda: randInt)))
_l_(350949)


def takeInput(message):
    _l_(350972)

    userInput = _c_(350952, _n_(350950, "input", lambda: input), _n_(350951, "message", lambda: message))
    _l_(350953)
    try:
        _l_(350971)

        userInput = _c_(350956, _n_(350954, "int", lambda: int), _n_(350955, "userInput", lambda: userInput))
        _l_(350957)
        _c_(350962, _n_(350958, "print", lambda: print), "takeInput try " + _c_(350961, _n_(350959, "str", lambda: str), _n_(350960, "userInput", lambda: userInput))) #This line is printing correct value every time
        _l_(350963) #This line is printing correct value every time
        aux = _n_(350964, "userInput", lambda: userInput)
        _l_(350965)
        return aux
    except _n_(350966, "ValueError", lambda: ValueError) as e:
        _l_(350970)

        _c_(350968, _n_(350967, "takeInput", lambda: takeInput), "Not a valid number, try again: ")
        _l_(350969)


userInput = _c_(350974, _n_(350973, "takeInput", lambda: takeInput), "Please enter a number: ")
_l_(350975)

while(not(_n_(350976, "userInput", lambda: userInput) == _n_(350977, "randInt", lambda: randInt))):
    _l_(350994)

    _c_(350982, _n_(350978, "print", lambda: print), "while loop " + _c_(350981, _n_(350979, "str", lambda: str), _n_(350980, "userInput", lambda: userInput))) #I am receiving a none value after I raise an exception and then enter a valid number
    _l_(350983) #I am receiving a none value after I raise an exception and then enter a valid number
    if(_n_(350984, "userInput", lambda: userInput) < _n_(350985, "randInt", lambda: randInt)):
        _l_(350992)

        userInput = _c_(350987, _n_(350986, "takeInput", lambda: takeInput), "Too small, try again : ")
        _l_(350988)
    else:
        userInput = _c_(350990, _n_(350989, "takeInput", lambda: takeInput), "Too large, try again : ")
        _l_(350991)
    count += 1
    _l_(350993)

_c_(350999, _n_(350995, "print", lambda: print), "Congratulations, you guessed it right in " + _c_(350998, _n_(350996, "str", lambda: str), _n_(350997, "count", lambda: count)) + " tries.")
_l_(351000)
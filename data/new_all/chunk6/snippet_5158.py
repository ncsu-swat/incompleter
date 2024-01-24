# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72299517/typeerror-in-python-in-custom-input-function-exception-handling
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(367205)

except ImportError:
    pass
randInt = _c_(367208, _a_(367207, _n_(367206, "random", lambda: random), "randint"), 1, 100)
_l_(367209)
count = 1
_l_(367210)
_c_(367215, _n_(367211, "print", lambda: print), "RandInt: " + _c_(367214, _n_(367212, "str", lambda: str), _n_(367213, "randInt", lambda: randInt)))
_l_(367216)


def takeInput(message):
    _l_(367239)

    userInput = _c_(367219, _n_(367217, "input", lambda: input), _n_(367218, "message", lambda: message))
    _l_(367220)
    try:
        _l_(367238)

        userInput = _c_(367223, _n_(367221, "int", lambda: int), _n_(367222, "userInput", lambda: userInput))
        _l_(367224)
        _c_(367229, _n_(367225, "print", lambda: print), "takeInput try " + _c_(367228, _n_(367226, "str", lambda: str), _n_(367227, "userInput", lambda: userInput))) #This line is printing correct value every time
        _l_(367230) #This line is printing correct value every time
        aux = _n_(367231, "userInput", lambda: userInput)
        _l_(367232)
        return aux
    except _n_(367233, "ValueError", lambda: ValueError) as e:
        _l_(367237)

        _c_(367235, _n_(367234, "takeInput", lambda: takeInput), "Not a valid number, try again: ")
        _l_(367236)


userInput = _c_(367241, _n_(367240, "takeInput", lambda: takeInput), "Please enter a number: ")
_l_(367242)

while(not(_n_(367243, "userInput", lambda: userInput) == _n_(367244, "randInt", lambda: randInt))):
    _l_(367261)

    _c_(367249, _n_(367245, "print", lambda: print), "while loop " + _c_(367248, _n_(367246, "str", lambda: str), _n_(367247, "userInput", lambda: userInput))) #I am receiving a none value after I raise an exception and then enter a valid number
    _l_(367250) #I am receiving a none value after I raise an exception and then enter a valid number
    if(_n_(367251, "userInput", lambda: userInput) < _n_(367252, "randInt", lambda: randInt)):
        _l_(367259)

        userInput = _c_(367254, _n_(367253, "takeInput", lambda: takeInput), "Too small, try again : ")
        _l_(367255)
    else:
        userInput = _c_(367257, _n_(367256, "takeInput", lambda: takeInput), "Too large, try again : ")
        _l_(367258)
    count += 1
    _l_(367260)

_c_(367266, _n_(367262, "print", lambda: print), "Congratulations, you guessed it right in " + _c_(367265, _n_(367263, "str", lambda: str), _n_(367264, "count", lambda: count)) + " tries.")
_l_(367267)
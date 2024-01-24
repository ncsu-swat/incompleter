# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21149842/nameerror-name-last-days-is-not-defined-trying-to-divide
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(664227)

except ImportError:
    pass

amount = _c_(664229, _n_(664228, "input", lambda: input), "Enter amount of medicine left: ")
_l_(664230)
dose = _c_(664232, _n_(664231, "input", lambda: input), "Enter dose per day: ")
_l_(664233)

def convertString(str):
    _l_(664247)

    try:
        _l_(664244)

        returnValue = _c_(664236, _n_(664234, "int", lambda: int), _n_(664235, "str", lambda: str))
        _l_(664237)
    except _n_(664238, "ValueError", lambda: ValueError):
        _l_(664243)

        returnValue = _c_(664241, _n_(664239, "float", lambda: float), _n_(664240, "str", lambda: str))
        _l_(664242)
    aux = _n_(664245, "returnValue", lambda: returnValue)
    _l_(664246)
    return aux

def count_days(amount, dose):
    _l_(664253)

    last_days = _n_(664248, "amount", lambda: amount) / _n_(664249, "dose", lambda: dose)
    _l_(664250)
    aux = _n_(664251, "last_days", lambda: last_days)
    _l_(664252)
    return aux

_c_(664256, _n_(664254, "print", lambda: print), "Your medicine will run out in ",_n_(664255, "last_days", lambda: last_days)," days.")
_l_(664257)
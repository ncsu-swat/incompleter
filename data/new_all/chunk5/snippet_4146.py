# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62344903/getting-nameerror-name-self-is-not-defined-while-executing-the-following-pr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class inputoutstring(_n_(697739, "object", lambda: object)):
    _l_(697743)


    def __init__(self):
        _l_(697742)

        _n_(697740, "self", lambda: self).s = ""
        _l_(697741)

class getstring(_n_(697744, "self", lambda: self)):
    _l_(697748)

    self.s = _c_(697746, _n_(697745, "input", lambda: input), "Enter the string for printing")
    _l_(697747)

class printstring(_n_(697749, "self", lambda: self)):
    _l_(697756)

    _c_(697754, _n_(697750, "print", lambda: print), _c_(697753, _a_(697752, _a_(697751, self, "s"), "upper")))
    _l_(697755)

str_obj = _c_(697758, _n_(697757, "inputoutstring", lambda: inputoutstring))
_l_(697759)

_c_(697762, _a_(697761, _n_(697760, "str_obj", lambda: str_obj), "getstring"))
_l_(697763)

_c_(697766, _a_(697765, _n_(697764, "str_obj", lambda: str_obj), "printstring")) 
_l_(697767) 
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74600872/attributeerror-list-object-has-no-attribute-lower-how-to-fix-the-code-in-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def removeDigits(str):
    _l_(374067)

    aux = _c_(374065, _a_(374061, _n_(374060, "str", lambda: str), "translate"), {_c_(374064, _n_(374062, "ord", lambda: ord), _n_(374063, "i", lambda: i)): None for i in '0123456789'})
    _l_(374066)
    return aux

def fileinput():
    _l_(374119)

    with _c_(374069, _n_(374068, "open", lambda: open), 'constant.txt') as f:
        _l_(374074)

        lines = _c_(374072, _a_(374071, _n_(374070, "f", lambda: f), "readlines"))
        _l_(374073)
    
    _c_(374077, _n_(374075, "print", lambda: print), 'Initial string: ', _n_(374076, "lines", lambda: lines))
    _l_(374078)
    res = _c_(374084, _n_(374079, "list", lambda: list), _c_(374083, _n_(374080, "map", lambda: map), _n_(374081, "removeDigits", lambda: removeDigits), _n_(374082, "lines", lambda: lines)))
    _l_(374085)
    _c_(374088, _n_(374086, "print", lambda: print), 'Final string: ', _n_(374087, "res", lambda: res))
    _l_(374089)
    
    _c_(374091, _n_(374090, "print", lambda: print), 'Make string upper or lower?')
    _l_(374092)
    choice = _c_(374094, _n_(374093, "input", lambda: input))
    _l_(374095)
    if _c_(374098, _a_(374097, _n_(374096, "choice", lambda: choice), "upper")) == 'UPPER':
        _l_(374118)

        _c_(374103, _n_(374099, "print", lambda: print), _c_(374102, _a_(374101, _n_(374100, "res", lambda: res), "upper")))
        _l_(374104)
    elif _c_(374107, _a_(374106, _n_(374105, "choice", lambda: choice), "lower")) == 'lower':
        _l_(374117)

        _c_(374112, _n_(374108, "print", lambda: print), _c_(374111, _a_(374110, _n_(374109, "res", lambda: res), "lower")))
        _l_(374113)
    else:
        _c_(374115, _n_(374114, "print", lambda: print), 'An error has occured')
        _l_(374116)

_c_(374121, _n_(374120, "fileinput", lambda: fileinput))
_l_(374122)
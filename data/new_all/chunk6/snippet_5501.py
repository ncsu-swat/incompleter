# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74600872/attributeerror-list-object-has-no-attribute-lower-how-to-fix-the-code-in-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def removeDigits(str):
    _l_(366998)

    aux = _c_(366996, _a_(366992, _n_(366991, "str", lambda: str), "translate"), {_c_(366995, _n_(366993, "ord", lambda: ord), _n_(366994, "i", lambda: i)): None for i in '0123456789'})
    _l_(366997)
    return aux

def fileinput():
    _l_(367050)

    with _c_(367000, _n_(366999, "open", lambda: open), 'constant.txt') as f:
        _l_(367005)

        lines = _c_(367003, _a_(367002, _n_(367001, "f", lambda: f), "readlines"))
        _l_(367004)
    
    _c_(367008, _n_(367006, "print", lambda: print), 'Initial string: ', _n_(367007, "lines", lambda: lines))
    _l_(367009)
    res = _c_(367015, _n_(367010, "list", lambda: list), _c_(367014, _n_(367011, "map", lambda: map), _n_(367012, "removeDigits", lambda: removeDigits), _n_(367013, "lines", lambda: lines)))
    _l_(367016)
    _c_(367019, _n_(367017, "print", lambda: print), 'Final string: ', _n_(367018, "res", lambda: res))
    _l_(367020)
    
    _c_(367022, _n_(367021, "print", lambda: print), 'Make string upper or lower?')
    _l_(367023)
    choice = _c_(367025, _n_(367024, "input", lambda: input))
    _l_(367026)
    if _c_(367029, _a_(367028, _n_(367027, "choice", lambda: choice), "upper")) == 'UPPER':
        _l_(367049)

        _c_(367034, _n_(367030, "print", lambda: print), _c_(367033, _a_(367032, _n_(367031, "res", lambda: res), "upper")))
        _l_(367035)
    elif _c_(367038, _a_(367037, _n_(367036, "choice", lambda: choice), "lower")) == 'lower':
        _l_(367048)

        _c_(367043, _n_(367039, "print", lambda: print), _c_(367042, _a_(367041, _n_(367040, "res", lambda: res), "lower")))
        _l_(367044)
    else:
        _c_(367046, _n_(367045, "print", lambda: print), 'An error has occured')
        _l_(367047)

_c_(367052, _n_(367051, "fileinput", lambda: fileinput))
_l_(367053)
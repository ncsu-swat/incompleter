# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51239898/can-we-use-closure-in-python-for-nested-function-but-it-is-giving-me-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def outerFunction(func):
    _l_(693947)

    def add(x,y):
        _l_(693938)

        _c_(693936, _n_(693933, "print", lambda: print), _n_(693934, "x", lambda: x)+_n_(693935, "y", lambda: y))
        _l_(693937)

    def sub(x,y):
        _l_(693944)

        _c_(693942, _n_(693939, "print", lambda: print), _n_(693940, "x", lambda: x)-_n_(693941, "y", lambda: y))
        _l_(693943)
    aux = _n_(693945, "func", lambda: func)
    _l_(693946)

    return aux

calc_add=_c_(693950, _n_(693948, "outerFunction", lambda: outerFunction), _n_(693949, "add", lambda: add))
_l_(693951)
calc_sub=_c_(693954, _n_(693952, "outerFunction", lambda: outerFunction), _n_(693953, "sub", lambda: sub))
_l_(693955)
_c_(693957, _n_(693956, "calc_add", lambda: calc_add), 56,60)
_l_(693958)
_c_(693960, _n_(693959, "calc_sub", lambda: calc_sub), 56,7)
_l_(693961)
# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56333872/adding-custom-number-class-to-python-int-results-in-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class IntType:
    _l_(457981)

    def __init__(self, value):
        _l_(457975)

        _n_(457972, "self", lambda: self).value = _n_(457973, "value", lambda: value)
        _l_(457974)

    def __add__(self, other):
        _l_(457980)

        aux = _a_(457977, _n_(457976, "self", lambda: self), "value") + _n_(457978, "other", lambda: other)
        _l_(457979)
        return aux

# Works
_c_(457985, _n_(457982, "print", lambda: print), _c_(457984, _n_(457983, "IntType", lambda: IntType), 10) + 10)
_l_(457986)

# Doesn't Work
_c_(457990, _n_(457987, "print", lambda: print), 10 + _c_(457989, _n_(457988, "IntType", lambda: IntType), 10))
_l_(457991)
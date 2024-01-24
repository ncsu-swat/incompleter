# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72383930/attributeerror-c-object-attribute-y-is-read-only-when-using-slots
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class C(_n_(638852, "object", lambda: object)):
    _l_(638859)

    __slots__ = ('x',)
    _l_(638853)
    def __init__(self, v):
        _l_(638857)

        _n_(638854, "self", lambda: self).x = _n_(638855, "v", lambda: v)
        _l_(638856)
    y = 123
    _l_(638858)

c = _c_(638861, _n_(638860, "C", lambda: C), 5)
_l_(638862)
_n_(638863, "c", lambda: c).y = 12
_l_(638864)
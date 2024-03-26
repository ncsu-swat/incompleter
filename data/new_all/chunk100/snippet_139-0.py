# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(102169)

    result = _c_(102165, _n_(102162, "sorted", lambda: sorted), _n_(102163, "lst", lambda: lst), key=lambda x: not _n_(102164, "x", lambda: x))
    _l_(102166)
    aux = _n_(102167, "result", lambda: result)
    _l_(102168)
    return aux
_c_(102171, _n_(102170, "print", lambda: print), '\nOriginal list:')
_l_(102172)
_c_(102175, _n_(102173, "print", lambda: print), _n_(102174, "nums", lambda: nums))
_l_(102176)
_c_(102178, _n_(102177, "print", lambda: print), '\nMove all zero digits to end of the said list of numbers:')
_l_(102179)
_c_(102184, _n_(102180, "print", lambda: print), _c_(102183, _n_(102181, "test", lambda: test), _n_(102182, "nums", lambda: nums)))
_l_(102185)
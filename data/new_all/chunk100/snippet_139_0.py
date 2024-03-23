# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(9720)

    result = _c_(9716, _n_(9713, "sorted", lambda: sorted), _n_(9714, "lst", lambda: lst), key=lambda x: not _n_(9715, "x", lambda: x))
    _l_(9717)
    aux = _n_(9718, "result", lambda: result)
    _l_(9719)
    return aux
_c_(9722, _n_(9721, "print", lambda: print), '\nOriginal list:')
_l_(9723)
_c_(9726, _n_(9724, "print", lambda: print), _n_(9725, "nums", lambda: nums))
_l_(9727)
_c_(9729, _n_(9728, "print", lambda: print), '\nMove all zero digits to end of the said list of numbers:')
_l_(9730)
_c_(9735, _n_(9731, "print", lambda: print), _c_(9734, _n_(9732, "test", lambda: test), _n_(9733, "nums", lambda: nums)))
_l_(9736)
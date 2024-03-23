# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_difference(l1, l2):
    _l_(8726)

    result = _c_(8715, _n_(8713, "list", lambda: list), _n_(8714, "l1", lambda: l1))
    _l_(8716)
    for el in _n_(8717, "l2", lambda: l2):
        _l_(8723)

        _c_(8721, _a_(8719, _n_(8718, "result", lambda: result), "remove"), _n_(8720, "el", lambda: el))
        _l_(8722)
    aux = _n_(8724, "result", lambda: result)
    _l_(8725)
    return aux
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8727)
_c_(8729, _n_(8728, "print", lambda: print), 'Original lists:')
_l_(8730)
_c_(8733, _n_(8731, "print", lambda: print), _n_(8732, "l1", lambda: l1))
_l_(8734)
_c_(8737, _n_(8735, "print", lambda: print), _n_(8736, "l2", lambda: l2))
_l_(8738)
_c_(8740, _n_(8739, "print", lambda: print), '\nDifference between two said list including duplicate elements):')
_l_(8741)
_c_(8747, _n_(8742, "print", lambda: print), _c_(8746, _n_(8743, "list_difference", lambda: list_difference), _n_(8744, "l1", lambda: l1), _n_(8745, "l2", lambda: l2)))
_l_(8748)
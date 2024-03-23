# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_difference(l1, l2):
    _l_(8762)

    result = _c_(8751, _n_(8749, "list", lambda: list), _n_(8750, "l1", lambda: l1))
    _l_(8752)
    for el in _n_(8753, "l2", lambda: l2):
        _l_(8759)

        _c_(8757, _a_(8755, _n_(8754, "result", lambda: result), "remove"), _n_(8756, "el", lambda: el))
        _l_(8758)
    aux = _n_(8760, "result", lambda: result)
    _l_(8761)
    return aux
l2 = [1, 1, 2, 4, 5, 6]
_l_(8763)
_c_(8765, _n_(8764, "print", lambda: print), 'Original lists:')
_l_(8766)
_c_(8769, _n_(8767, "print", lambda: print), _n_(8768, "l1", lambda: l1))
_l_(8770)
_c_(8773, _n_(8771, "print", lambda: print), _n_(8772, "l2", lambda: l2))
_l_(8774)
_c_(8776, _n_(8775, "print", lambda: print), '\nDifference between two said list including duplicate elements):')
_l_(8777)
_c_(8783, _n_(8778, "print", lambda: print), _c_(8782, _n_(8779, "list_difference", lambda: list_difference), _n_(8780, "l1", lambda: l1), _n_(8781, "l2", lambda: l2)))
_l_(8784)
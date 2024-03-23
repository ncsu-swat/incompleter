# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_difference(l1, l2):
    _l_(8794)

    for el in _n_(8785, "l2", lambda: l2):
        _l_(8791)

        _c_(8789, _a_(8787, _n_(8786, "result", lambda: result), "remove"), _n_(8788, "el", lambda: el))
        _l_(8790)
    aux = _n_(8792, "result", lambda: result)
    _l_(8793)
    return aux
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8795)
l2 = [1, 1, 2, 4, 5, 6]
_l_(8796)
_c_(8798, _n_(8797, "print", lambda: print), 'Original lists:')
_l_(8799)
_c_(8802, _n_(8800, "print", lambda: print), _n_(8801, "l1", lambda: l1))
_l_(8803)
_c_(8806, _n_(8804, "print", lambda: print), _n_(8805, "l2", lambda: l2))
_l_(8807)
_c_(8809, _n_(8808, "print", lambda: print), '\nDifference between two said list including duplicate elements):')
_l_(8810)
_c_(8816, _n_(8811, "print", lambda: print), _c_(8815, _n_(8812, "list_difference", lambda: list_difference), _n_(8813, "l1", lambda: l1), _n_(8814, "l2", lambda: l2)))
_l_(8817)
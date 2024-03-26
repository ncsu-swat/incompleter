# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_difference(l1, l2):
    _l_(101778)

    result = _c_(101767, _n_(101765, "list", lambda: list), _n_(101766, "l1", lambda: l1))
    _l_(101768)
    for el in _n_(101769, "l2", lambda: l2):
        _l_(101775)

        _c_(101773, _a_(101771, _n_(101770, "result", lambda: result), "remove"), _n_(101772, "el", lambda: el))
        _l_(101774)
    aux = _n_(101776, "result", lambda: result)
    _l_(101777)
    return aux
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(101779)
_c_(101781, _n_(101780, "print", lambda: print), 'Original lists:')
_l_(101782)
_c_(101785, _n_(101783, "print", lambda: print), _n_(101784, "l1", lambda: l1))
_l_(101786)
_c_(101789, _n_(101787, "print", lambda: print), _n_(101788, "l2", lambda: l2))
_l_(101790)
_c_(101792, _n_(101791, "print", lambda: print), '\nDifference between two said list including duplicate elements):')
_l_(101793)
_c_(101799, _n_(101794, "print", lambda: print), _c_(101798, _n_(101795, "list_difference", lambda: list_difference), _n_(101796, "l1", lambda: l1), _n_(101797, "l2", lambda: l2)))
_l_(101800)
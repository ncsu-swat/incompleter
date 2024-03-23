# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pairwise(l1):
    _l_(50197)

    temp = []
    _l_(50178)
    for i in _c_(50183, _n_(50179, "range", lambda: range), _c_(50182, _n_(50180, "len", lambda: len), _n_(50181, "l1", lambda: l1)) - 1):
        _l_(50194)

        (current_element, next_element) = (_n_(50184, "l1", lambda: l1)[_n_(50185, "i", lambda: i)], _n_(50186, "l1", lambda: l1)[_n_(50187, "i", lambda: i) + 1])
        _l_(50188)
        _c_(50192, _a_(50190, _n_(50189, "temp", lambda: temp), "append"), _n_(50191, "x", lambda: x))
        _l_(50193)
    aux = _n_(50195, "temp", lambda: temp)
    _l_(50196)
    return aux
l1 = [1, 1, 2, 3, 3, 4, 4, 5]
_l_(50198)
_c_(50200, _n_(50199, "print", lambda: print), 'Original lists:')
_l_(50201)
_c_(50204, _n_(50202, "print", lambda: print), _n_(50203, "l1", lambda: l1))
_l_(50205)
_c_(50207, _n_(50206, "print", lambda: print), '\nIterate over all pairs of consecutive items of the said list:')
_l_(50208)
_c_(50213, _n_(50209, "print", lambda: print), _c_(50212, _n_(50210, "pairwise", lambda: pairwise), _n_(50211, "l1", lambda: l1)))
_l_(50214)
# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pairwise(l1):
    _l_(50275)

    for i in _c_(50258, _n_(50254, "range", lambda: range), _c_(50257, _n_(50255, "len", lambda: len), _n_(50256, "l1", lambda: l1)) - 1):
        _l_(50272)

        (current_element, next_element) = (_n_(50259, "l1", lambda: l1)[_n_(50260, "i", lambda: i)], _n_(50261, "l1", lambda: l1)[_n_(50262, "i", lambda: i) + 1])
        _l_(50263)
        x = (_n_(50264, "current_element", lambda: current_element), _n_(50265, "next_element", lambda: next_element))
        _l_(50266)
        _c_(50270, _a_(50268, _n_(50267, "temp", lambda: temp), "append"), _n_(50269, "x", lambda: x))
        _l_(50271)
    aux = _n_(50273, "temp", lambda: temp)
    _l_(50274)
    return aux
l1 = [1, 1, 2, 3, 3, 4, 4, 5]
_l_(50276)
_c_(50278, _n_(50277, "print", lambda: print), 'Original lists:')
_l_(50279)
_c_(50282, _n_(50280, "print", lambda: print), _n_(50281, "l1", lambda: l1))
_l_(50283)
_c_(50285, _n_(50284, "print", lambda: print), '\nIterate over all pairs of consecutive items of the said list:')
_l_(50286)
_c_(50291, _n_(50287, "print", lambda: print), _c_(50290, _n_(50288, "pairwise", lambda: pairwise), _n_(50289, "l1", lambda: l1)))
_l_(50292)
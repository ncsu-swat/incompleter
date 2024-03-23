# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_index(l1):
    _l_(24725)

    aux = _c_(24723, _n_(24719, "sum", lambda: sum), (1 for i in _n_(24720, "l1", lambda: l1) if _n_(24721, "i", lambda: i) > 45 and _n_(24722, "i", lambda: i) % 2 == 0))
    _l_(24724)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(24726)
_c_(24728, _n_(24727, "print", lambda: print), 'Original list:')
_l_(24729)
_c_(24732, _n_(24730, "print", lambda: print), _n_(24731, "nums", lambda: nums))
_l_(24733)
_c_(24736, _n_(24734, "print", lambda: print), '\nNumber of Items of the said list which are even and greater than', _n_(24735, "n", lambda: n))
_l_(24737)
_c_(24742, _n_(24738, "print", lambda: print), _c_(24741, _n_(24739, "first_index", lambda: first_index), _n_(24740, "nums", lambda: nums)))
_l_(24743)
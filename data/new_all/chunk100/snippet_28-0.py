# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_index(l1):
    _l_(108276)

    aux = _c_(108274, _n_(108270, "sum", lambda: sum), (1 for i in _n_(108271, "l1", lambda: l1) if _n_(108272, "i", lambda: i) > 45 and _n_(108273, "i", lambda: i) % 2 == 0))
    _l_(108275)
    return aux
_c_(108278, _n_(108277, "print", lambda: print), 'Original list:')
_l_(108279)
_c_(108282, _n_(108280, "print", lambda: print), _n_(108281, "nums", lambda: nums))
_l_(108283)
n = 45
_l_(108284)
_c_(108287, _n_(108285, "print", lambda: print), '\nNumber of Items of the said list which are even and greater than', _n_(108286, "n", lambda: n))
_l_(108288)
_c_(108293, _n_(108289, "print", lambda: print), _c_(108292, _n_(108290, "first_index", lambda: first_index), _n_(108291, "nums", lambda: nums)))
_l_(108294)
# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def addition_subtrction(x, y):
    _l_(69767)

    aux = (_n_(69762, "x", lambda: x) + _n_(69763, "y", lambda: y), _n_(69764, "x", lambda: x) - _n_(69765, "y", lambda: y))
    _l_(69766)
    return aux
nums1 = [6, 5, 3, 9]
_l_(69768)
_c_(69770, _n_(69769, "print", lambda: print), 'Original lists:')
_l_(69771)
_c_(69774, _n_(69772, "print", lambda: print), _n_(69773, "nums1", lambda: nums1))
_l_(69775)
_c_(69778, _n_(69776, "print", lambda: print), _n_(69777, "nums2", lambda: nums2))
_l_(69779)
result = _c_(69784, _n_(69780, "map", lambda: map), _n_(69781, "addition_subtrction", lambda: addition_subtrction), _n_(69782, "nums1", lambda: nums1), _n_(69783, "nums2", lambda: nums2))
_l_(69785)
_c_(69787, _n_(69786, "print", lambda: print), '\nResult:')
_l_(69788)
_c_(69793, _n_(69789, "print", lambda: print), _c_(69792, _n_(69790, "list", lambda: list), _n_(69791, "result", lambda: result)))
_l_(69794)
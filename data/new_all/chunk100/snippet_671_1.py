# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def addition_subtrction(x, y):
    _l_(69800)

    aux = (_n_(69795, "x", lambda: x) + _n_(69796, "y", lambda: y), _n_(69797, "x", lambda: x) - _n_(69798, "y", lambda: y))
    _l_(69799)
    return aux
nums2 = [0, 1, 7, 7]
_l_(69801)
_c_(69803, _n_(69802, "print", lambda: print), 'Original lists:')
_l_(69804)
_c_(69807, _n_(69805, "print", lambda: print), _n_(69806, "nums1", lambda: nums1))
_l_(69808)
_c_(69811, _n_(69809, "print", lambda: print), _n_(69810, "nums2", lambda: nums2))
_l_(69812)
result = _c_(69817, _n_(69813, "map", lambda: map), _n_(69814, "addition_subtrction", lambda: addition_subtrction), _n_(69815, "nums1", lambda: nums1), _n_(69816, "nums2", lambda: nums2))
_l_(69818)
_c_(69820, _n_(69819, "print", lambda: print), '\nResult:')
_l_(69821)
_c_(69826, _n_(69822, "print", lambda: print), _c_(69825, _n_(69823, "list", lambda: list), _n_(69824, "result", lambda: result)))
_l_(69827)
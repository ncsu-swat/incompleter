# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(102362)

except ImportError:
    pass

def remove_duplicates(nums):
    _l_(102372)

    result = _c_(102368, _a_(102364, _n_(102363, "functools", lambda: functools), "reduce"), lambda x, y: _n_(102365, "x", lambda: x) * _n_(102366, "y", lambda: y), _n_(102367, "nums", lambda: nums), 1)
    _l_(102369)
    aux = _n_(102370, "result", lambda: result)
    _l_(102371)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(102373)
_c_(102376, _n_(102374, "print", lambda: print), 'list1:', _n_(102375, "nums1", lambda: nums1))
_l_(102377)
_c_(102379, _n_(102378, "print", lambda: print), 'Product of the said list numbers:')
_l_(102380)
_c_(102385, _n_(102381, "print", lambda: print), _c_(102384, _n_(102382, "remove_duplicates", lambda: remove_duplicates), _n_(102383, "nums1", lambda: nums1)))
_l_(102386)
_c_(102389, _n_(102387, "print", lambda: print), '\nlist2:', _n_(102388, "nums2", lambda: nums2))
_l_(102390)
_c_(102392, _n_(102391, "print", lambda: print), 'Product of the said list numbers:')
_l_(102393)
_c_(102398, _n_(102394, "print", lambda: print), _c_(102397, _n_(102395, "remove_duplicates", lambda: remove_duplicates), _n_(102396, "nums2", lambda: nums2)))
_l_(102399)
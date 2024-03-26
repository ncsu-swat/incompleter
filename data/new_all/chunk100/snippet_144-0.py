# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(102323)

except ImportError:
    pass

def remove_duplicates(nums):
    _l_(102333)

    result = _c_(102329, _a_(102325, _n_(102324, "functools", lambda: functools), "reduce"), lambda x, y: _n_(102326, "x", lambda: x) * _n_(102327, "y", lambda: y), _n_(102328, "nums", lambda: nums), 1)
    _l_(102330)
    aux = _n_(102331, "result", lambda: result)
    _l_(102332)
    return aux
nums2 = [2.2, 4.12, 6.6, 8.1, 8.3]
_l_(102334)
_c_(102337, _n_(102335, "print", lambda: print), 'list1:', _n_(102336, "nums1", lambda: nums1))
_l_(102338)
_c_(102340, _n_(102339, "print", lambda: print), 'Product of the said list numbers:')
_l_(102341)
_c_(102346, _n_(102342, "print", lambda: print), _c_(102345, _n_(102343, "remove_duplicates", lambda: remove_duplicates), _n_(102344, "nums1", lambda: nums1)))
_l_(102347)
_c_(102350, _n_(102348, "print", lambda: print), '\nlist2:', _n_(102349, "nums2", lambda: nums2))
_l_(102351)
_c_(102353, _n_(102352, "print", lambda: print), 'Product of the said list numbers:')
_l_(102354)
_c_(102359, _n_(102355, "print", lambda: print), _c_(102358, _n_(102356, "remove_duplicates", lambda: remove_duplicates), _n_(102357, "nums2", lambda: nums2)))
_l_(102360)